# program_04_Movie_ticket_booking.py

class MovieTicket:

    def __init__(self, movie_name, seats, price):
        self.movie_name = movie_name
        self.seats = seats
        self.price = price

    def total_amount(self):
        total = self.seats * self.price

        print("Movie :", self.movie_name)
        print("Seats :", self.seats)
        print("Total Amount :", total)


movie = input("Enter Movie Name : ")
seats = int(input("Enter Number of Seats : "))
price = int(input("Enter Ticket Price : "))

obj = MovieTicket(movie, seats, price)

obj.total_amount()