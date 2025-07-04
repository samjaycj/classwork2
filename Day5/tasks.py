import time

def long_task():
    print("Long task: running slowly")
    time.sleep(3)
    print("Long task: finished")

def short_task():
    print("Short task: running quick")
    time.sleep(.5)
    print("Short task: finished")

print("......Program without threads........")

short_task()
long_task()
short_task()
