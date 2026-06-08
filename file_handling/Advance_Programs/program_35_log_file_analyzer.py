# program_35_log_file_analyzer.py

count = 0

with open("log.txt", "r") as file:

    for line in file:

        if "ERROR" in line:
            count += 1

print("Total Errors :", count)