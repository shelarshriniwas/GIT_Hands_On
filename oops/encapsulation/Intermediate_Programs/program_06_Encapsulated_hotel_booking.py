# program_06_Encapsulated_hotel_booking.py

class Hotel:

    def __init__(self):

        self.__rooms = 10

    def book_room(self):

        if self.__rooms > 0:

            self.__rooms -= 1

            print("Room Booked")

        else:

            print("No Rooms Available")

    def available_rooms(self):

        print("Rooms Left :", self.__rooms)


obj = Hotel()

obj.book_room()

obj.available_rooms()