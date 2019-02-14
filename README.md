# Cython Basics 
A PoC to understand and use Cython

## Advantages, in my opinion, of using Cython
* Transforms your *.py* modules into high-performant *C* files, and these *C* files can be compiled as native binary libraries effortlessly.
* Better code protection than *.pyc*, which can be reverse-engineered. When the compilation is completed, there’s no way to reverse compiled libraries back to readable Python source code.

## How to have a feel of it on a Virtual Environment

**My Environment**: *Ubuntu 18.04.2 LTS - Python 3.7.2*

### Steps to reproduce it

##### 1. Create a Virtual Environment
```bash
$ python3 -m venv env

$ source env/bin/activate
```

##### 2. Install the Cython package
```bash
$ pip install cython
```

##### 3. Create *compile.py* as in the example. It will use *hello_world.py* and *what_time_is_it.py* as modules.

###### 3.1. hello_world.py
```python
def say_hello():

    print("Hello World!")

if __name__ == '__main__':
    say_hello()
```
###### 3.2. what_time_is_it.py
```python
from datetime import datetime

def give_me_the_time():

    print("It is {}:{}".format(datetime.now().hour,datetime.now().minute))

if __name__ == '__main__':
    give_me_the_time()
```
###### 3.3. compile.py
```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("hello_world",  ["hello_world.py"]),
    Extension("what_time_is_it",  ["what_time_is_it.py"]),
    #   ... all your modules that need be compiled ...
]

setup(
    name = 'Cython Basics',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
```

##### 4. Run compile.py 
```bash
$ python compile.py build_ext
```

This will output *.so* binary files on a **_build/lib.linux-x86_64-3.7_** subfolder in my case (which are the ones you may want to distribute) and *.c* files in my main folder for each module included in compile.py

##### 5. Use the generated binary files

###### 5.1. Switch to the output folder
```bash
$ cd build/lib.linux-x86_64-3.7
```
###### 5.2. Create a file *run_modules.py* within that folder to include the modules
```python
from hello_world import say_hello
from what_time_is_it import give_me_the_time

def main():

    say_hello()
    give_me_the_time()

if __name__ == '__main__':
    main()
```

###### 5.3. Run it
```bash
$ python run_modules.py
```

This will output the print statements defined on each module.


### Additional Notes

+ *.py* and *.c* files can now be removed if you don need them.
+ The *.so* files contain the target platform in their names (e.g. linux-x86_64-3.7). These compiled modules are not cross-platform. You may want to compile a platform-specific version of your code for each of your targeted platforms.
+ I left the files as they finished on my folders for this PoC, except for the *env* directory used for the Virtual Environment.