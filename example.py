import random
from HeapTree import *

# Create an array of random numbers
array = [random.randint(0, 100) for i in range(10)]

# Create a heap tree
heap = HeapTree(array)

# Print the array
print(heap.array)

# Sort the tree in max heap method
heap.max_heapify()

# Print the array
print(heap.array)

# Sort the tree in min heap method
heap.min_heapify()

# Print the array
print(heap.array)

# Print the maximum value
print(heap.max_extract())

# Print the minimum value
print(heap.min_extract())
