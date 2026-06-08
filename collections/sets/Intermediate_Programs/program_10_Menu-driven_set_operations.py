# program_10_Menu-driven_set_operations.py

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

while True:
    print("\n\n",set1)
    print(set2)
    print("\n1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Symmetric Difference")
    print("5. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        print("Union :", set1 | set2)

    elif choice == 2:
        print("Intersection :", set1 & set2)

    elif choice == 3:
        print("Difference :", set1 - set2)

    elif choice == 4:
        print("Symmetric Difference :", set1 ^ set2)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")