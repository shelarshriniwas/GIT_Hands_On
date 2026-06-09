'''
Input
{'A':45,'B':20,'C':70}
Output
B
'''
data = {'A':45,'B':20,'C':70}

min_key = ""

min_value = float("inf")

for k,v in data.items():
    if v < min_value:
        min_value = v
        min_key = k

print(min_key)