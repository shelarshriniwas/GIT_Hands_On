# program_20_search_form.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def search():

    query = request.args.get("query")

    if query:
        return f"Search Result For : {query}"

    return """
    <form method="get">

        Search:
        <input type="text" name="query">

        <input type="submit" value="Search">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)