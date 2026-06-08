# program_06_Hospital_management_system.py
class Hospital:

    def doctor(self, fees):

        if fees >= 500 and fees <= 1000:
            print("First Time visited")

        else:
            print("Seconf Time visited")

obj = Hospital()

obj.doctor(950)