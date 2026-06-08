# Student marks statistics.
import statistics

marks = []

for i in range(5):

    mark = int(input("Enter Mark : "))

    marks.append(mark)

print("Mean :", statistics.mean(marks))
print("Median :", statistics.median(marks))
print("Highest :", max(marks))
print("Lowest :", min(marks))