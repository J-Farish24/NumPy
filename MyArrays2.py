import numpy as np

# 4 rows and 3 columns
# Row = student, column = exam
# student0, student1, student2, student3
# test0, test1, test2
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])


# Indexing and slicing
student1 = grades[1]

student_0_test_1 = grades[0, 1]

students0_1 = grades[0:2]

students1and3 = grades[[1, 3]]
students1and3_test2 = grades[[1, 3], 2]

all_students_test0 = grades[:, 0]

all_student_test1_2 = grades[:, 1:3]

all_students_test0_2 = grades[:, [0, 2]]

grades_2 = np.array(np.random.randint(60, 100, 12)).reshape(3, 4)

grades_2.mean()
# By col
grades_2.mean(axis=0)
# By row
grades_2.mean(axis=1)

numbers = np.arange(1, 6)
numbers_view = numbers.view()

numbers[1] *= 10


numbers_slice_view = numbers[0:3]

numbers[1] *= 20


numbers_copy = numbers.copy()

numbers[1] *= 10


grades = np.array([[87, 96, 70], [100, 87, 90]])
grades_reshaped = grades.reshape(1, 6)
# grades.resize(1, 6)

flattened = grades.flatten()

raveled = grades.ravel()

raveled[0] = 100
raveled[5] = 100

print()
