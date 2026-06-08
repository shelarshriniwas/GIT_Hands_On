# program_40_resume_data_parser.py

import re

with open("resume.txt", "r") as file:

    data = file.read()

emails = re.findall(r'\S+@\S+', data)

print(emails)