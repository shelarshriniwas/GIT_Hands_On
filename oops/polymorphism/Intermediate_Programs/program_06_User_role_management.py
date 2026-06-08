# program_06_User_role_management.py

class Manager:

    def dashboard(self):

        print("Manager Dashboard")


class Employee:

    def dashboard(self):

        print("Employee Dashboard")


m = Manager()
e = Employee()

m.dashboard()
e.dashboard()