from flask import Flask, render_template

from flask_homework.main import main
from flask_homework.fruits import fruits
from flask_homework.vegetables import vegetables

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
