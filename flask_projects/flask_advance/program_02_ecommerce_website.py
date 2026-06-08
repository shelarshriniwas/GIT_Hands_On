# program_02_ecommerce_website.py

from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"id":1,"name":"Laptop","price":50000},
    {"id":2,"name":"Mobile","price":20000},
    {"id":3,"name":"Headphones","price":3000}
]

@app.route("/")
def home():

    html = """
    <h1>E-Commerce Store</h1>

    {% for p in products %}
        <h3>{{p.name}}</h3>
        Price : ₹{{p.price}}
        <hr>
    {% endfor %}
    """

    return render_template_string(html, products=products)

if __name__ == "__main__":
    app.run(debug=True)