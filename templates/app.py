from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data= {
        "name": "John",
        "age": 25,
        "city": "Mumbai"
    }

    return render_template("index.html", user=data)

if __name__ == "__main__":
    app.run(debug=True)