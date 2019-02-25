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

### Helper functions 
def list_offences():
    offences = Request(**{ 'endpoint': '/list-offences/', 'data': '', 'headers': ''})
    offences_list = offences.get()
    print(offences_list)
    return offences_list

def list_reviews():
    reviews = Request(**{ 'endpoint': '/review/', 'data': '', 'headers': ''})
    reviews_list = reviews.get()
    print(reviews_list)
    return reviews_list

def current_user_details():
    print(session['token'])
    body = {'endpoint': '/user/', 'data': {}, 'header': {'Authorization': 'Token  {0}'.format(session['token'])}}
    user = Request(**body)
    return user.get()

### Routes

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
        auth_response = authenticate.post()
        session['token'] = auth_response['token']
        print(session['token'])

        headers = {'Authorization': 'Token {0}'.format(session['token'])}
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

@bp.route('/lawyers/register', methods=['GET','POST'])
def lawyers_registration():
    if request.method == 'POST':
        data = request.form 
        body = request_body
        userdata = {
            'username': data['username'],
            'password': data['password'],
            'email': ''
            }
        print(">>> Authenticate and get user details")
        body['endpoint'], body['data'], body['headers'] = '/register/', userdata, {'Content-Type': 'application/json'}
        authenticate = Request(**body)
        reg_user = authenticate.post()
        print(">>>> Auth user: {0}".format(reg_user))
        user_info = {
            "user": int(reg_user['id']),
            "practise_number": data['practice_number'],
            "building_address": data['building_address'],
            "street_road": data['street_road'],
            "building_floor": data['building_floor'],
            "id_number": data['id_number'],
            "phone_number": data['phone_number']
        }
        print(">>> Add more lawyer information")
        body['endpoint'], body['data'], body['headers'] = '/add-lawyer/', user_info, {'Content-Type': 'application/json'}
        update_profile = Request(**body)
        user_info = update_profile.post()
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