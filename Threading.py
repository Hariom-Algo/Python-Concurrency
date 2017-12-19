import threading
import time

def threadWorker():
    print("My thread has entered the Running state")
    time.sleep(10)
    print("My work is done")

myThread = threading.Thread(target=threadWorker)
myThread.start()
myThread.join()
print("Thread Entered the dead state")