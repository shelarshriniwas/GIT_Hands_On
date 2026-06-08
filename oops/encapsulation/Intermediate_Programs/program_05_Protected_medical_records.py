# program_05_Protected_medical_records.py

class Hospital:

    def __init__(self):

        self.__report = "Blood Test Normal"

    def get_report(self):

        return self.__report


obj = Hospital()

print(obj.get_report())