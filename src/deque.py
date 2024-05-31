"""
deque (pronounced "deck") stands for "double-ended queue". 
It is a data structure from the collections module in Python that allows 
you to add and remove elements from both ends efficiently.

deque is particularly useful for algorithms that require frequent additions and
removals from both ends of a list, such as implementing queues, stacks, 
or sliding window algorithms.
"""

from collections import deque

# Create a deque
d = deque([1, 2, 3, 4, 5])

# Append to the right
d.append(6)  # deque([1, 2, 3, 4, 5, 6])
print(d)

# Append to the left
d.appendleft(0)  # deque([0, 1, 2, 3, 4, 5, 6])
print(d)

# Pop from the right
d.pop()  # returns 6, deque([0, 1, 2, 3, 4, 5])
print(d)

# Pop from the left
d.popleft()  # returns 0, deque([1, 2, 3, 4, 5])
print(d)

# Extend the right end
d.extend([6, 7, 8])  # deque([1, 2, 3, 4, 5, 6, 7, 8])
print(d)

# Extend the left end
d.extendleft([-2, -1])  # deque([-1, -2, 1, 2, 3, 4, 5, 6, 7, 8])
print(d)

# Rotate the deque to the right by 3 steps
d.rotate(3)  # deque([6, 7, 8, -1, -2, 1, 2, 3, 4, 5])
print(d)

# Rotate the deque to the left by 2 steps
d.rotate(-2)  # deque([8, -1, -2, 1, 2, 3, 4, 5, 6, 7])
print(d)