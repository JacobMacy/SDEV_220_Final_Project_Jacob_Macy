from flask import Flask, render_template, request, redirect, url_for
from models import League

app = Flask(__name__)

leagues = []

@app.route("/", methods=["GET", "POST"])
def index():
    error = ""

    if request.method == "POST":
        try:
            league = League(request.form.get("name", ""))

            if any(item.name.lower() == league.name.lower() for item in leagues):
                raise ValueError("That league already exists.")

            leagues.append(league)
            return redirect(url_for("index"))

        except ValueError as message:
            error = str(message)

    return render_template("index.html", leagues=leagues, error=error)

@app.route("/add-bowler/<int:league_id>", methods=["POST"])
def add_bowler(league_id):
    if not 0 <= league_id < len(leagues):
        return render_template(
            "index.html",
            leagues=leagues,
            error="League not found."
        )

    try:
        name = request.form.get("name", "")
        leagues[league_id].add_bowler(name)

    except ValueError as message:
        return render_template(
            "index.html",
            leagues=leagues,
            error=str(message)
        )

    return redirect(url_for("index"))

@app.route("/add-game/<int:league_id>/<int:bowler_id>", methods=["POST"])
def add_game(league_id, bowler_id):
    error = ""

    if not 0 <= league_id < len(leagues):
        error = "League not found."
    else:
        bowler = leagues[league_id].bowlers.get(bowler_id)

        if bowler is None:
            error = "Bowler not found."
        else:
            try:
                score = int(request.form.get("score", ""))
                bowler.add_game(score)
                return redirect(url_for("index"))
            #This only allows valid bowling scores to be entered
            except ValueError:
                error = "Score must be a whole number from 0 to 300."

    return render_template("index.html", leagues=leagues, error=error)

if __name__ == "__main__":
    app.run()