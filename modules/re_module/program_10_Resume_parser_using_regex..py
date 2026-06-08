import re

resume = """
Name: Rahul
Email: rahul@gmail.com
Phone: 9876543210
"""

email = re.findall(r"[\w\.-]+@[\w\.-]+", resume)
phone = re.findall(r"\d{10}", resume)

print("Email:", email)
print("Phone:", phone)