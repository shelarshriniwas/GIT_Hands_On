'''
Program 1.Count_Character_Frequency
text = "python"
Output:
{'p':1,'y':1,'t':1,'h':1,'o':1,'n':1}

'''

s = input("Ente the string: ")
dict = {}

for i in s:
    if i in dict:
        dict[i] +=1 
    else:
        dict[i] = 1

print("Frequency of char: ",dict)