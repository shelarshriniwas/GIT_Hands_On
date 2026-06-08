# Compare averages.
import statistics

class_a = [70, 80, 90]
class_b = [60, 75, 85]

avg_a = statistics.mean(class_a)
avg_b = statistics.mean(class_b)

print("Class A Average :", avg_a)
print("Class B Average :", avg_b)

if avg_a > avg_b:
    print("Class A Has Higher Average")

else:
    print("Class B Has Higher Average")