# program_01_Banking_system.py

accounts = {
    101: {
        "name": "Rahul",
        "balance": 5000
    }
}

withdraw = 2000

if accounts[101]["balance"] >= withdraw:

    accounts[101]["balance"] -= withdraw

    print("Remaining Balance :",
          accounts[101]["balance"])

else:
    print("Insufficient Balance")