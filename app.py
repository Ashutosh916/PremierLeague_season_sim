from flask import Flask, render_template, request
from simulator import simulate_season, final_table

app = Flask(__name__)

# Default league teams + OVRs
default_teams = {
    "Arsenal": 86, "Chelsea": 83, "Liverpool": 87, "Man City": 90, "Man United": 85,
    "Tottenham": 84, "Newcastle": 82, "Aston Villa": 81, "West Ham": 80, "Brighton": 79,
    "Everton": 77, "Leicester": 78, "Southampton": 76, "Wolves": 77, "Crystal Palace": 76,
    "Fulham": 78, "Brentford": 77, "Bournemouth": 75, "Nottingham Forest": 74, "Leeds": 75
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_team = request.form.get("team")
        # reset team data
        teams = {
            name: {"name": name, "OVR": ovr, "MP": 0, "W": 0, "D": 0, "L": 0,
                   "GF": 0, "GA": 0, "Pts": 0}
            for name, ovr in default_teams.items()
        }
        history = simulate_season(teams)
        table_display, _ = final_table(teams)

        return render_template("results.html",
                               user_team=user_team,
                               table=table_display.to_dict(orient="records"),
                               history=history)
    return render_template("index.html", teams=default_teams.keys())

if __name__ == "__main__":
    app.run(debug=True)