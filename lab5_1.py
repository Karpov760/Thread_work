import operator
from time import sleep
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from multiprocessing import Pool
from random import randint
import copy

#класс Node для определения элемента списка
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList\n [ ' + str(current.value) + ' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    def InsertNth(self, i, x): #i - index, x - value
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr != None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next

    def BubbleSort(self):
        a = Node(0, None)
        b = Node(0, None)
        c = Node(0, None)
        e = Node(0, None)
        tmp = Node(0, None)

        while (e != self.first.next):
            c = a = self.first
            b = a.next

            while a != e:
                if a and b:
                    if a.value > b.value:
                        if a == self.first:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            self.first = b
                            c = b
                        else:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            c.next = b
                            c = b
                    else:
                        c = a
                        a = a.next
                    b = a.next
                    if b == e:
                        e = a
                else:
                    e = a



    def len(self):
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first

    def get_index(self, x):
        length = -1
        if self.first != None:
            current = self.first
            while current.next != None and current.value != x:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first

    def get_value(self, i):
        count = -1
        if self.first != None:
            current = self.first
            while count != i:
                count += 1
                value = current.value
                try:
                    current = current.next
                except:
                    break
        return value

    def set_value(self, i, x):
        count = 0
        if self.first != None:
            current = self.first
            while current.next != None and count != i:
                current = current.next
                count += 1
            current.value = x


    def swap(self, i1, i2):
        value1 = self.get_value(i1)
        value2 = self.get_value(i2)
        self.set_value(i2,value1)
        self.set_value(i1,value2)



    def __getitem__(self, key):  # поддержка обращения по ключу
        length = 0
        current = None
        if self.first != None:
            current = self.first
            while key != length or current.next != None:
                current = current.next
                length += 1
            if key == length: current = current.value
        return current



if __name__=="__main__":
    L = LinkedList()
    #for i in range(0, 10):
    #    L.add(randint(0, 20))
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(5)
    L.add(4)
    print(L)

    print('Sorted list: ', end='')
    print(L)
