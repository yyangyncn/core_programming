import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Thread start:" + self.name)
        print_time(self.name, self.counter, 5)
        print("Thread exit:" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        print("thradname:delay:counter", threadName, delay, counter)
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{0}:{1}".format(threadName, time.ctime(time.time())))
        print()
        counter -= 1

thread1 = myThread(1, "Thread1", 1)
thread2 = myThread(2, "Thread2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exit main thread")