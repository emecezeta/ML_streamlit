from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("/workspaces/Appwebs/models/salary_predictor_model.sav", "rb"))


@app.route("/", methods = ["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        
        data = [[val1, val2, val3]]
        salary = model.predict(data)[0]
        rounded_salary = round(salary, -3)
        prediction = f"${rounded_salary:,.0f} dólares"
    
    return render_template("index.html", prediction=prediction)