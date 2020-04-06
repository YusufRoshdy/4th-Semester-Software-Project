from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('main', __name__)

@bp.route('/', methods=('GET',))
@login_required
def dropdown():
    colours = ['Profile', 'Timetable', 'Survey', 'Contact']
    return render_template('main/index.html', colours=colours)