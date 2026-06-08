# program_31_bank_transaction_log_system.py

with open("transactions.txt", "a") as file:

    transaction = input("Enter Transaction : ")

    file.write(transaction + "\n")

print("Transaction Saved")