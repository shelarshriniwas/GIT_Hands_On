# program_02_Coordinate_point_calculator.py

point1 = (2, 3)

point2 = (5, 7)

distance = (
    (point2[0] - point1[0]) ** 2 +
    (point2[1] - point1[1]) ** 2
) ** 0.5

print(distance)