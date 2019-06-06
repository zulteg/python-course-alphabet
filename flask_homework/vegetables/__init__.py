from flask import Blueprint, render_template

from flask_homework.utils import FileManager

vegetables = Blueprint('vegetables', __name__, template_folder='templates')


@vegetables.route("/vegetables")
def list_page():
    return render_template("vegetables_list.html",
                           items=FileManager.load_data('vegetables'))


@vegetables.route("/vegetables/add", methods=["POST"])
def add_item():
    return 'success' if FileManager.add_item('vegetables') else 'error'


@vegetables.route("/vegetables/rm", methods=["POST"])
def rm_item():
    return 'success' if FileManager.rm_item('vegetables') else 'error'
