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


if __name__ == "__main__":
    app.run()