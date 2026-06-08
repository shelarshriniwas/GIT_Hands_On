# program_09_Ticket_booking_system.py

class TrainBooking:

    def train_info(self):

        print("Train : Rajdhani Express")


class Passenger(TrainBooking):

    def passenger_name(self):

        print("Passenger : Shriniwas")


obj = Passenger()

obj.train_info()
obj.passenger_name()