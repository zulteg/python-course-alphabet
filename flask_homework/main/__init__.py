from flask import Blueprint, render_template, url_for, redirect

main = Blueprint('main', __name__, template_folder='templates')


@main.route("/")
def home_page():
    return render_template("home.html")


@main.route("/redirect-to-main")
def redirect_to_main():
    return redirect(url_for('main.home_page'), 301)
