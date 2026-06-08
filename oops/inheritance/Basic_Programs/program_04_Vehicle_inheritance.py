# program_04_Vehicle_inheritance.py

class Vehicle:

    def start(self):

        print("Vehicle Starts")


class Car(Vehicle):

    def speed(self):

        print("Car Speed is 120 km/h")


obj = Car()

obj.start()
obj.speed()