# program_05_URL_validator.py
import re

url = "https://google.com"

if url.startswith("http://") or \
   url.startswith("https://"):

    print("Valid URL")

else:
    print("Invalid URL")



url2 = "https://google.com"

pattern2 = r'https?://\S+'

if re.match(pattern2, url2):
    print("Valid URL")

else:
    print("Invalid URL")