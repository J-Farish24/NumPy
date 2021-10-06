import numpy as np
import random

arr01 = np.array([[1, 2, 3], [4, 5, 6]])

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
"""
for row in arr01:
    print(row)
    for column in row:
        print(column, end=" ")
    print()

for i in arr01.flat:
    print(i)
"""

arr03 = np.zeros(5)

arr04 = np.ones((2, 4), dtype=int)

arr05 = np.full((3, 5), 13)

print()

# Create 2 dimensional array of 5 random integer elements using list comprehension
a = np.array(
    [
        [random.randint(1, 10) for num in range(5)],
        [random.randint(1, 10) for num in range(5)],
    ]
)
b = np.array(np.random.randint(1, 10, size=(2, 5)))
print(a)
print(b)

arr06 = np.arange(5)

arr07 = np.arange(5, 10)

arr08 = np.arange(10, 1, -2)

print()
