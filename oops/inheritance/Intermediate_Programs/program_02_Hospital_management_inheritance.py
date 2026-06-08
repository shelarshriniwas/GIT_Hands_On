# program_02_Hospital_management_inheritance.py

class Hospital:

    def hospital_name(self):

        print("City Hospital")


class Doctor(Hospital):

    def doctor_info(self):

        print("Doctor : Cardiologist")


obj = Doctor()

obj.hospital_name()
obj.doctor_info()