from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html',
                           title='Boda Justice')


@bp.route('/login')
def login():
    return render_template('main/index.html',
                            title='Boda Justice')

@bp.route('/lawyers')
def lawyers_dashboard():
    return render_template('lawyers/index.html',
                            title='Boda Justice',
                            logged_in=True)

@bp.route('/lawyers/register')
def lawyers_registration():
    return render_template('lawyers/registration.html',
                            title='Boda Justice')

@bp.route('/complainants')
def complainants_dashboard():
    return render_template('complainants/index.html',
                            title='Boda Justice',
                            logged_in=True)

@bp.route('/complainants/register')
def complainants_registration():
    return render_template('complainants/registration.html',
                            title='Boda Justice')