# program_03_food_ordering_system.py

from flask import Flask, request, render_template_string

app = Flask(__name__)

menu = {
    "Pizza":300,
    "Burger":150,
    "Pasta":250
}

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        item = request.form["item"]
        qty = int(request.form["qty"])

        total = menu[item] * qty

        return f"Order Placed<br>Total = ₹{total}"

    html = """
    <h2>Food Ordering System</h2>

    <form method="post">

    Item:
    <select name="item">
        <option>Pizza</option>
        <option>Burger</option>
        <option>Pasta</option>
    </select>

    Quantity:
    <input type="number" name="qty">

    <input type="submit">

    </form>
    """

    return html

if __name__ == "__main__":
    app.run(debug=True)