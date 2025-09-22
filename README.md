# PremierLeague_season_sim
⚽ Premier League Season Simulator

A simple Python + Flask web app that simulates a full premier league season.
You can select your favorite team, run the season, and view the final league table.

✨ Features

20 teams play a full season (home & away fixtures).

Results are based on team strength (OVR), not just random rolls.

Points system follows real football rules (Win = 3, Draw = 1, Loss = 0).

Final table shows: Points, Wins, Draws, Losses, Goal Difference.

Top 4 qualify for Champions League, bottom 3 are relegated.

Simple and clean Bootstrap frontend (with placeholder team logos).

Fully customizable:

Edit team names in app.py.

Adjust team OVRs for realism.

Add your own logos in static/.

🚀 How to Run Locally

Clone the repo:

Install dependencies:

pip install flask

Run the app:

python app.py

Open in browser:

http://127.0.0.1:5000/

📂 Project Structure
pl_simulator/
│── app.py              # Main Flask app
│── requirements.txt    # Dependencies (Flask)
│── static/
│    └── style.css      # Styling
│── templates/
     ├── index.html     # Team selection page
     └── results.html   # Final league table + results
