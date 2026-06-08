import re

text = "Python #aws #docker #python"

tags = re.findall(r"#\w+", text)

print(tags)