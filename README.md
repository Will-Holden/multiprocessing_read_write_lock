# multiprocessing_read_write_lock
a read write lock, which can be used in multiprocess envirment
# 多进程下读写锁
## 使用方法
在主进程中创建读写锁， 作为参数传入到子进程中。
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
