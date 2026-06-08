import re

text = "Python123 AWS456 Docker789"

numbers = re.findall(r"\d+", text)

print(numbers)