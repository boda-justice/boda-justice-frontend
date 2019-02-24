from flask import (
    Blueprint, render_template, request, redirect, session
)

from app.services.apicalls import Request

bp = Blueprint('main', __name__)

request_body = {
    'endpoint': '',
    'data': '',
    'headers': ''
}

@bp.route('/', methods=['GET'])
def index():
    return redirect('/login')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form 
        body = request_body
        body['endpoint'], body['data'], body['headers'] = '/login/', {'username': data['username'], 'password': data['password']}, {'Content-Type': 'application/json'}
        authenticate = Request(**body)
        token = authenticate.post()
        session['token'] = token
        print(session['token'])
        headers = {'Content-Type': 'application/json', 'Authorization': 'Token {0}'.format(session['token'])}
        body = {'endpoint': '/user/', 'headers': headers, 'data': {}}
        user_profile = Request(**body)
        print(user_profile.get())

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
@bp.route('/test-offences', methods=['GET'])
def list_offences():
    offences = Request(**{ 'endpoint': '/list-offences/', 'data': '', 'headers': ''})
    offences_list = offences.get()
    print(offences_list)
    return offences_list