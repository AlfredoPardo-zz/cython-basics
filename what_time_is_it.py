from datetime import datetime

def give_me_the_time():

    print("It is {}:{}".format(datetime.now().hour,datetime.now().minute))

if __name__ == '__main__':
    give_me_the_time()