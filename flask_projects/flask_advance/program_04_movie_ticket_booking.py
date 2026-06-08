# program_04_movie_ticket_booking.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        movie = request.form["movie"]
        seats = request.form["seats"]

        return f"""
        Booking Successful<br>
        Movie : {movie}<br>
        Seats : {seats}
        """

    return """
    <h2>Movie Ticket Booking</h2>

    <form method="post">

    Movie:
    <input type="text" name="movie"><br><br>

    Seats:
    <input type="number" name="seats"><br><br>

    <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)