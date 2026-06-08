import re

text = "Visit https://google.com and http://aws.com"

urls = re.findall(r"https?://\S+", text)

print(urls)