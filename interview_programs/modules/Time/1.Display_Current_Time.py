'''
Program 1.Display_Current_Time.py

Output:

HH:MM:SS
'''

from datetime import datetime

now = datetime.now().time()
print("Current Time : ",now)