from flask import Flask, render_template
import pandas as pd

app = Flask("website")


@app.route("/")
def home():
    df = pd.read_csv("data_small/stations.txt", skiprows=17)
    df= df[["STAID", "STANAME                                 "]]

    return render_template("home.html", data=df.to_html())


@app.route("/API/v1/<station>/<date>")
def about(station, date):
    date = f"{date[:4]}-{(date[4:6])}-{(date[6:])}"
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == (date)]['   TG'].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


app.run(debug=True)
