import time
import threading

def long_task():
    print("Long task: running slowly")
    time.sleep(3)
    print("Long task: finished")

def short_task():
    print("Short task: running quick")
    time.sleep(.5)
    print("Short task: finished")

def longer_task():
    print("Very Long task: running slowly for 5 seconds")
    time.sleep(5)
    print("very Long task: finished")

background_thread = threading.Thread(target=long_task)
longer_thread = threading.Thread(target=longer_task)
longer_thread.start()
background_thread.start()

short_task()
short_task()

background_thread.join()
longer_thread.join()

print("......Program with threads completed........")