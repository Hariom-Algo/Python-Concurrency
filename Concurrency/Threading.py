import threading
import time

def threadWorker():
    print("My thread has entered the Running state")
    time.sleep(10)
    print("My work is done")

def threadWorker1():
    print("My thread 1 has entered the Running state ")
    time.sleep(5)
    print("My thread 1 work is done")

myThread = threading.Thread(target=threadWorker)
myThread1 = threading.Thread(target=threadWorker1)
myThread.start()
myThread1.start()
myThread.join()
myThread1.join()
print("Thread Entered the dead state")