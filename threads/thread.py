import threading


def new():
    for x in range(10):
        print('Single Thread')


t1 = threading.Thread(target=new)

t1.start()
t1.join()
print('Success')