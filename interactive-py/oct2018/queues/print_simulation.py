from pythonds.basic.queue import Queue

from queues.printer import Printer
from queues.task import Task

import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average wait {:.2f} secs, {} tasks remaining".format(averageWait, printQueue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    return num == 180

for i in range(10):
    simulation(3600, 5)
