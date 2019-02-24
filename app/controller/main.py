from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html',
                           title='Boda Justice')

@bp.route('/lawyers')
def lawyers_dashboard():
    return render_template('lawyers/index.html',
                            title='Boda Justice',
                            logged_in=True)

@bp.route('/login')
def login():
    return render_template('main/index.html',
                            title='Boda Justice')
