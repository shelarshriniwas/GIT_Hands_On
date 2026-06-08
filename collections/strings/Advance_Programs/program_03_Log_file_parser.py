# program_03_Log_file_parser.py

logs = """
INFO Server Started
ERROR Database Failed
ERROR Login Failed
"""

count = logs.count("ERROR")

print(count)



logs = """
INFO Server Started
ERROR Database Failed
ERROR Login Failed
"""

for line in logs.splitlines():

    if "ERROR" in line:
        print(line)