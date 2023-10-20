"""Simple Flask app to demonstrate some testing."""

from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"


@app.route('/')
def index():
    """Show homepage."""

    # Keep a count of how many times page is visited
    session['count'] = session.get('count', 0) + 1

    return render_template("index.html")


@app.route('/fav-color', methods=['POST'])
def fav_color():
    """Show favorite color."""

    fav_color = request.form.get('color')

    return render_template("color.html", fav_color=fav_color)


@app.route('/redirect-me')
def redirect_me():
    """Redirect user to homepage."""

    return redirect("/")
# with redirects, it doesnt immediately go to the redirect page:
# 1. first GET request to redirect-me
# 2. gives a response code of 302 and also the response includes the new location to make the 2nd request to
# 3. browser automatically make the new request to new route
#  can check how this works with curl -v 127.../redirect-me
