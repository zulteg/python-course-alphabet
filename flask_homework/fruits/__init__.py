from flask import Blueprint, render_template

from flask_homework.utils import FileManager

fruits = Blueprint('fruits', __name__, template_folder='templates')


@fruits.route("/fruits")
def list_page():
    return render_template("fruits_list.html",
                           items=FileManager.load_data('fruits'))


@fruits.route("/fruits/add", methods=["POST"])
def add_item():
    return 'success' if FileManager.add_item('fruits') else 'error'


@fruits.route("/fruits/rm", methods=["POST"])
def rm_item():
    return 'success' if FileManager.rm_item('fruits') else 'error'
