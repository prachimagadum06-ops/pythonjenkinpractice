from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data= [
        {"name": "John","age": 25,"city": "Mumbai"},
        {"name": "Suja","age": 40,"city": "Mumbai"},
        {"name": "Prachi","age": 20,"city": "Pune"},
        {"name": "uday","age": 45,"city": "Pune"},
          {"name": "mahesh","age": 55,"city": "Pune"}
    ]

    return render_template("index.html", user=data)

if __name__ == "__main__":
    app.run(debug=True)