#
# Max Base
# 2023-02-03
# https://github.com/BaseMax/StepByStepHeapTreePy
#

class HeapTree:
    def __init__(self, array):
        self.array = array
        self.heapify()
    
    def max_heapify(self):
        for i in range(len(self.array)):
            self.max_heapify_index(i)
        
    def max_heapify_index(self, index):
        left = self.left(index)
        right = self.right(index)
        largest = index
        if left < len(self.array) and self.array[left] > self.array[largest]:
            largest = left
        if right < len(self.array) and self.array[right] > self.array[largest]:
            largest = right
        if largest != index:
            self.array[largest], self.array[index] = self.array[index], self.array[largest]
            self.max_heapify_index(largest)
    
    def min_heapify(self):
        for i in range(len(self.array)):
            self.min_heapify_index(i)
    
    def min_heapify_index(self, index):
        left = self.left(index)
        right = self.right(index)
        smallest = index
        if left < len(self.array) and self.array[left] < self.array[smallest]:
            smallest = left
        if right < len(self.array) and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != index:
            self.array[smallest], self.array[index] = self.array[index], self.array[smallest]
            self.min_heapify_index(smallest)
    
    def min_insert(self, value):
        self.array.append(value)
        self.min_heapify()
    
    def max_insert(self, value):
        self.array.append(value)
        self.max_heapify()
    
    def min_extract(self):
        if len(self.array) == 0:
            return None
        value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.min_heapify()
        return value
    
    def max_extract(self):
        if len(self.array) == 0:
            return None
        value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.max_heapify()
        return value
