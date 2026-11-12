from flask import Flask, render_template, request
from tip_calculator import calculate_tip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        bill = float(request.form["bill"])
        tip = int(request.form["tip"])
        people = int(request.form["people"])

        grand_total, final_amount = calculate_tip(bill, tip, people)

        return render_template("index.html", grand_total=grand_total, final_amount=final_amount)
    
    return render_template("index.html",grand_total=None, final_amount=None)

if __name__ == "__main__":
    app.run(debug=True)
