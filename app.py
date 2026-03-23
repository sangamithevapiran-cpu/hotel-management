from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bill(days, room_type):
    if room_type == "Standard":
        price = 1000
    elif room_type == "Deluxe":
        price = 2000
    elif room_type == "AC":
        price = 3000
    else:
        price = 0
    
    return days * price

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    
    if request.method == "POST":
        name = request.form["name"]
        days = int(request.form["days"])
        room_type = request.form["room"]
        
        total = calculate_bill(days, room_type)
    
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)