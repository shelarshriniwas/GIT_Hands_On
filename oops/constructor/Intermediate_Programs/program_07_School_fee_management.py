# program_07_School_fee_management.py

class StudentFee:

    def __init__(self, student_name, total_fee, paid_fee):
        self.student_name = student_name
        self.total_fee = total_fee
        self.paid_fee = paid_fee

    def remaining_fee(self):

        balance = self.total_fee - self.paid_fee

        print("Student :", self.student_name)
        print("Total Fee :", self.total_fee)
        print("Paid Fee :", self.paid_fee)
        print("Remaining Fee :", balance)


name = input("Enter Student Name : ")
total = int(input("Enter Total Fee : "))
paid = int(input("Enter Paid Fee : "))

obj = StudentFee(name, total, paid)

obj.remaining_fee()