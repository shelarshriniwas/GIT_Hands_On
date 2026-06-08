# program_09_Hotel_booking_system.py

class Hotel:

    def room(self, no):
        amount = 200
        if no >= 1 and no <= 10:
            amount = no*200
            print(f" {no} : Rooms available and will booked and amount will be: {amount} ")

        else:
            print("Rooms not available")

obj = Hotel()

obj.room(9)