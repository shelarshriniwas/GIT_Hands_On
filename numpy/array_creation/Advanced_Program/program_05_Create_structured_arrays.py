# program_05_Create_structured_arrays.py

import numpy as np

students = np.array([
    (1,"Ram",85),
    (2,"Shyam",90),
    (3,"Mohan",88)
],
dtype=[
    ('id','i4'),
    ('name','U10'),
    ('marks','i4')
])

print(students)