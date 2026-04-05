from flask import Flask, render_template, request
import requests

app = Flask(__name__)
                                                                                                                 
@app.route("/", methods=["GET", "POST"])
def home():
    suggestion = ""
    temperature = None
    error = ""

    if request.method == "POST":
        city_name = request.form["city"]
        api_key = "631d27da5d0d3a21ee007f543e4fca75"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"      
        response = requests.get(url).json()

        if response.get("cod") == 200 or response.get("cod") == "200":
            temperature = response["main"]["temp"]

            if temperature > 25:
                suggestion = "Its hot today! Wear a T-shirt and shorts."
            elif temperature > 15:
                suggestion = "Pleasant weather! Wear a light shirt or hoodie."
            else:
                suggestion = "Its cold today! Wear a jacket and warm clothes."
        else:
            error = "Please Enter a valid city name."

    return render_template("index.html",suggestion=suggestion,temperature=temperature,error=error)

if __name__ == "__main__":
    app.run(debug=True)