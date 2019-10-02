from flask import *
import server

app = Flask(__name__)
Server = None


@app.route('/', methods=['POST', 'GET'])
def login():
    if 'session' not in request.cookies.keys():
        return render_template('login.html')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            response = make_response(redirect('/dashboard'))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', Server.get_permission(new_token))
            return response
        else:
            return render_template('login.html')


@app.route('/authen', methods=['POST'])
def authenticate():
    form = request.form
    username = form.get('uname')
    password = form.get('psw')
    result, token = Server.login_password(username, password)
    if result == 0:
        response = make_response(redirect('/dashboard'))
        response.set_cookie('session', token)
        response.set_cookie('account_type', Server.get_permission(token))
        return response
    else:
        return redirect('/')


@app.route('/index', methods=['POST', 'GET'])
def get_form_data():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('add_question.html', search_results={})


@app.route('/add', methods=['POST', "GET"])
def add():
    files = request.files
    form = request.form
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            Server.add_question(form, files)
            response = make_response('success')
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', Server.get_permission(new_token))
            return response
        else:
            return redirect('/')


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            response = make_response(render_template('dashboard.html', search_results={}))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', Server.get_permission(new_token))
            return response
        else:
            return redirect('/')


@app.route('/account_setting', methods=['POST', 'GET'])
def account_settings():
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            response = make_response(render_template('account_setting.html'))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', Server.get_permission(new_token))
            return response
        else:
            return render_template('login.html')


@app.route('/bulk_upload', methods=['POST', 'GET'])
def bulk_page():
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            response = make_response(render_template('bulk_upload.html'))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', Server.get_permission(new_token))
            return response
        else:
            return render_template('login.html')


@app.route('/bulk_submit', methods=['POST', 'GET'])
def bulkapi():
    files = request.files
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            file = files.get('buck_questions')
            Server.bulk_upload(file)
            response = make_response('success')
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', Server.get_permission(new_token))
            return response
        else:
            return redirect('/')


@app.route('/search', methods=['POST', 'GET'])
def query_page():
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            response = make_response(render_template('search_questions.html'))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type',
                                Server.get_permission(new_token))
            return response
        else:
            return redirect('/')


@app.route('/query', methods=['POST', 'GET'])
def query():
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = Server.login_token(token)
        if result:
            key_word = request.form['key_word']
            question = Server.search_by_serial_number(key_word)
            response = make_response(render_template('search_questions.html', search_results=question))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type',
                                Server.get_permission(new_token))
            return response
            pass
        else:
            return redirect('/')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        Server.logout(token)
        return redirect('/')


if __name__ == '__main__':
    Server = server.Server()
    app.run(host='localhost', port=5000)
