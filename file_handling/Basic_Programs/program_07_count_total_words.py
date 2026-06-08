# program_07_count_total_words.py


path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"


with open(path2,"r") as f1:
    data = f1.read().split()

print("Total words in file: ",len(data))