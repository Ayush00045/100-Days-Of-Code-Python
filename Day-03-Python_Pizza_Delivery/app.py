from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    total = None
    error = None
    size_name = ""
    pepperoni_price = 0
    cheese_price = 0

    if request.method == "POST":

        size = request.form.get("size")
        pepperoni = request.form.get("pepperoni")
        extra_cheese = request.form.get("extra_cheese")

        bill = 0

        # Pizza Size
        if size == "S":
            bill += 15
            size_name = "Small Pizza"

        elif size == "M":
            bill += 20
            size_name = "Medium Pizza"

        elif size == "L":
            bill += 25
            size_name = "Large Pizza"

        else:
            error = "Invalid Pizza Size!"

        # Pepperoni
        if error is None and pepperoni == "Y":

            if size == "S":
                pepperoni_price = 2
            else:
                pepperoni_price = 3

            bill += pepperoni_price

        # Extra Cheese
        if error is None and extra_cheese == "Y":
            cheese_price = 1
            bill += cheese_price

        if error is None:
            total = bill

    return render_template(
        "index.html",
        total=total,
        error=error,
        size_name=size_name,
        pepperoni_price=pepperoni_price,
        cheese_price=cheese_price
    )


if __name__ == "__main__":
    app.run(debug=True)