from fei.ppds import Event
from random import randint as rand
from fei.ppds import Thread, Semaphore, Mutex
from time import sleep
from fei.ppds import print


class Fibannoci:
    def __init__(self, numberOfThreads):
        self.numberOfThreads = numberOfThreads
        self.actualPosition = 1
        self.fibannociList = [0, 1]
        self.semaphoreList = []

        for _ in range(numberOfThreads):
            self.semaphoreList.append(Semaphore(0))
        self.semaphoreList[0].signal()

    def count_two_fibannoci_numbers(self):
        return (self.fibannociList[self.actualPosition - 1] +
                self.fibannociList[self.actualPosition - 2])

    def fibannoci_counter_semaphore(self, thread_id):
        self.semaphoreList[thread_id].wait()

        self.actualPosition += 1
        self.fibannociList.append(self.count_two_fibannoci_numbers())

        if thread_id < self.numberOfThreads-1:
            self.semaphoreList[self.actualPosition-1].signal()


def start(f, thread_id):

    print("Thread %d done" % thread_id)
    print(f.fibannociList)


numberOfThreads = 20
f = Fibannoci(numberOfThreads)

threads = list()

for i in range(numberOfThreads):
    t = Thread(start, f, i)
    threads.append(t)

for t in threads:
    t.join()
