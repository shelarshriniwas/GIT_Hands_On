import re

text = "Visit https://google.com and https://github.com"

urls = re.findall(r'https?://\S+', text)

print(urls)