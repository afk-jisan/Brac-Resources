# -*- coding: utf-8 -*-
"""Graph basic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B-2UywQXAkUpGsBtvQno-sWtnBX9qFtn
"""

import numpy as np

class MaxHeap:
  def __init__(self, capacity):
    self.heap = np.zeros(capacity, dtype=int)
    self.size = 0

  def insert(self, val):
    if self.size == len(self.heap) - 1:
      print("No space left")
      return
    self.size += 1
    self.heap[self.size] = val
    self.__swim()

  def __swim(self):
    parent = self.size // 2
    index = self.size
    while parent > 0 and self.heap[index] >= self.heap[parent]:
      temp = self.heap[parent]
      self.heap[parent] = self.heap[index]
      self.heap[index] = temp
      index = parent
      parent = index // 2

  def delete(self):
    if self.size == 0:
      print("No Item Left in heap")
      return "All Done"
    temp = self.heap[1]
    self.heap[1] = self.heap[self.size]
    self.heap[self.size] = temp
    self.size -= 1
    self.__sink()

  def __sink(self):
    index = 1
    left = 2 * index
    right = 2 * index + 1
    while left <= self.size and right <= self.size:
      if self.heap[left] >= self.heap[index] and self.heap[right] >= self.heap[index]:
        if self.heap[left] > self.heap[right]:
          max = left
        else:
          max = right
        temp = self.heap[index]
        self.heap[index] = self.heap[max]
        self.heap[max] = temp
        index = max
      elif self.heap[left] >= self.heap[index]:
        temp = self.heap[index]
        self.heap[index] = self.heap[left]
        self.heap[left] = temp
        index = left

      elif self.heap[right] >= self.heap[index]:
        temp = self.heap[index]
        self.heap[index] = self.heap[right]
        self.heap[right] = temp
        index = right

      else:
        return

      left = 2 * index
      right = 2 * index + 1

    if left <= self.size:
      if self.heap[left] >= self.heap[index]:
        temp = self.heap[index]
        self.heap[index] = self.heap[left]
        self.heap[left] = temp

  def printArray(self):
    for i in range(len(self.heap)):
      print(self.heap[i], end=' ')
    print("\nDone printing the array. Heap size is:", self.size)


val = [10, 27, 9, 33, 30]
max_heap = MaxHeap(8)
max_heap.printArray()

for i in range(len(val)):
  max_heap.insert(val[i])
  max_heap.printArray()

print("\n")
print("Now I will delete all the items")


while True:
  var = max_heap.delete()
  max_heap.printArray()
  if var == "All Done":
    break

import numpy as np
class MinHeap:
  def __init__(self, capacity):
    self.heap = np.zeros(capacity, dtype=int)
    self.size = 0

  def printArray(self):
    print(f"Min Heap [size: {self.size}]: {self.heap}")

  def insert(self, val):
    if self.size == len(self.heap) - 1:
      print("No Size left")
      return "error"

    self.size += 1
    self.heap[self.size] = val
    self.__swim()

  def __swim(self):
    index = self.size
    parent = index // 2
    while parent > 0 and self.heap[parent] > self.heap[index]:
      temp = self.heap[parent]
      self.heap[parent] = self.heap[index]
      self.heap[index] = temp
      index = parent
      parent = index // 2

  def delete(self):
    if self.size == 0:
      print("No More item in heap")
      return "Error"
    val = self.heap[1]
    self.heap[1] = self.heap[self.size]
    self.heap[self.size] = val
    self.size -= 1
    self.__sink()

  def __sink(self):
    parent = 1
    left = 2 * parent
    right = 2 * parent + 1
    while left <= self.size and right <= self.size:
      if self.heap[parent] > self.heap[left] and self.heap[parent] > self.heap[right]:
        if self.heap[left] < self.heap[right]:
          temp = self.heap[parent]
          self.heap[parent] = self.heap[left]
          self.heap[left] = temp
          parent = left
        else:
          temp = self.heap[parent]
          self.heap[parent] = self.heap[right]
          self.heap[right] = temp
          parent = right

      elif self.heap[parent] > self.heap[left]:
        temp = self.heap[parent]
        self.heap[parent] = self.heap[left]
        self.heap[left] = temp
        parent = left

      elif self.heap[parent] > self.heap[right]:
        temp = self.heap[parent]
        self.heap[parent] = self.heap[right]
        self.heap[right] = temp
        parent = right

      else:
        break

      left = 2 * parent
      right = 2 * parent + 1

    if left <= self.size and self.heap[parent] > self.heap[left]:
      temp = self.heap[parent]
      self.heap[parent] = self.heap[left]
      self.heap[left] = temp


arr = [0, 5, 50, 10, 60, 55, 15, 20, 65]
min_heap = MinHeap(15)
min_heap.printArray()

for i in range(1, len(arr)):
  min_heap.insert(arr[i])

min_heap.printArray()
min_heap.insert(4)
min_heap.printArray()


print()
print()
min_heap.delete()
min_heap.printArray()

while True:
  if min_heap.delete() != "Error":
    min_heap.printArray()
  else:
    break

import numpy as np
class MaxHeap:
    def __init__(self, capacity):
        self.heap = np.zeros(capacity, dtype = int)
        self.size = 0

    def printArray(self):
        print(f"Max Heap [size: {self.size}]: {self.heap[1:self.size+1]}")

    def insert(self, val):
        if self.size == len(self.heap) - 1:
            print("No more capacity in the heap")
            return "Error"
        self.size += 1
        self.heap[self.size] = val
        self.__swim()

    def __swim(self):
        child = self.size
        parent = child // 2
        while parent > 0 and self.heap[parent] < self.heap[child]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = temp
            child = parent
            parent = child // 2

    def delete(self):
        if self.size == 0:
            print("No item in heap")
            return "Error"
        temp = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = temp
        self.size -= 1
        self.__sink()

    def __sink(self):
        parent = 1
        left = 2 * parent
        right = 2 * parent + 1
        while left <= self.size and right <= self.size:
            if self.heap[parent] < self.heap[left] and self.heap[parent] < self.heap[right]:
                if self.heap[left] > self.heap[right]:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[left]
                    self.heap[left] = temp
                    parent = left
                else:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[right]
                    self.heap[right] = temp
                    parent = right
            elif self.heap[parent] < self.heap[left]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[left]
                self.heap[left] = temp
                parent = left
            elif self.heap[parent] < self.heap[right]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[right]
                self.heap[right] = temp
                parent = right

            else:
                break
            left = 2 * parent
            right = 2 * parent + 1

        if left <= self.size and self.heap[parent] < self.heap[left]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[left]
            self.heap[left] = temp


arr = [0, 100, 50, 70, 30, 40, 60, 65, -10, 20, 25]
max_heap = MaxHeap(12)

max_heap.printArray()
for i in range(1, len(arr)):
    max_heap.insert(arr[i])

max_heap.printArray()

max_heap.insert(800)

max_heap.printArray()
print("\n")
while True:
    if max_heap.delete() != "Error":
        max_heap.printArray()
    else:
        break

import numpy as np
class MinHeap:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__heap = np.zeros(capacity,dtype=int)
        self.__size = 0


    def __swim(self, index):
        if index == 0:
            return

        parent = (index - 1) // 2
        if self.__heap[index] < self.__heap[parent]:
            self.__heap[index], self.__heap[parent] = self.__heap[parent], self.__heap[index]
            self.__swim(parent)

    def __sink(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < self.__size and self.__heap[left_child] < self.__heap[smallest]:
            smallest = left_child
        if right_child < self.__size and self.__heap[right_child] < self.__heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.__heap[index], self.__heap[smallest] = self.__heap[smallest], self.__heap[index]
            self.__sink(smallest)

    def insert(self, value):
        if self.__size == self.__capacity:
            return

        self.__heap[self.__size] = value
        self.__swim(self.__size)
        self.__size += 1

    def extract_min(self,i):
        if self.__size == 0:
            return
        self.__sink(0)
        min_value = self.__heap[0]
        self.__heap[0] = self.__heap[self.__size - 1]
        self.__size -= 1
        return min_value


    def show_array(self):
        #print(f"Min Heap [size: {self.__size}]: {self.__heap[1:self.__size+1]}")
        print(f"Min Heap [size: {self.__size}]: {self.__heap}")



arr = [0, 100, 50, 70, 30, 40, 60, 65, -10, 20, 25]
heap = MinHeap(12)

heap.show_array()
for i in range(1, len(arr)):
    heap.insert(arr[i])
heap.show_array()