import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing.sharedctypes import Value
from multiprocessing import Process
from rwlock.rwlock import RWLock
import os

# l = multiprocessing_utils.local()
# l.lock = multiprocessing_utils.SharedLock()
# l.lock1 = multiprocessing_utils.SharedLock()
# lock = multiprocessing.Lock()


class MyManger(BaseManager):
    pass


def Manager():
    m = MyManger()
    m.start()
    return m


def f(name, lock):
    # lock.writer_lock.acquire()
    lock.reader_lock.acquire()
    try:
            while True:
                print(name)
                print(lock)
                print(os.getpid())
    except:
            print("error")


def f2(name, lock):
    # lock.writer_lock.acquire()
    lock.reader_lock.acquire()
    try:
            while True:
                # a = count.get()
                print(name)
                print(lock)
                print(os.getpid())
                # print(lock.get_condition())
    except Exception as e:
        print(e)
        print("error")


if __name__ == '__main__':
    lock = RWLock()
    a1 = Process(target=f, args=("hee", lock,))
    a2 = Process(target=f2, args=("there", lock,))
    a1.start()
    a2.start()
    a1.join()
    a2.join()
