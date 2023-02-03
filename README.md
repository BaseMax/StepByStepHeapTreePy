# StepByStep Heap-Tree in Python

A step-by-step implementation of a heap-tree in Python. By this class you can easily convert an array to maxheap or minheap tree. Also you can extract the maximum or minimum value from the heap-tree.

The heap-tree is a binary tree that can be used to sort an array of numbers. The heap-tree is a complete binary tree, which means that all levels of the tree are filled except possibly the last level. The last level is filled from left to right.

## Example

```python
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
```
