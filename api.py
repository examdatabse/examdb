from flask import *
import examdb.app
import traceback
import examdb.docs
import examdb.server
app = Flask(__name__)
server = None


@app.route('/', methods=['POST', 'GET'])
def login():
    if 'session' not in request.cookies.keys():
        return render_template('login.html')
    else:
        token = request.cookies['session']
        result, new_token = server.login_token(token)
        if result:
            response = make_response(redirect('/dashboard'))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', server.get_permission(new_token))
            return response
        else:
            return render_template('login.html')


@app.route('/authen', methods=['POST'])
def authenticate():
    form = request.form
    username = form.get('uname')
    password = form.get('psw')
    result, token = server.login_password(username, password)
    if result == 0:
        response = make_response(redirect('/dashboard'))
        response.set_cookie('session', token)
        response.set_cookie('account_type', server.get_permission(token))
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
    if not session.get('logged_in'):
        return redirect('/')
    files = request.files
    form = request.form
    print(files)
    try:
        examdb.app.add_questions(form, files)
    except Exception:
        traceback.print_exc()
    return "Added"


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    print(request.cookies)
    if 'session' not in request.cookies.keys():
        return redirect('/')
    else:
        token = request.cookies['session']
        result, new_token = server.login_token(token)
        if result:
            response = make_response(render_template('dashboard.html', search_results={}))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', server.get_permission(new_token))
            return response
        else:
            return redirect('/')


@app.route('/account_setting', methods=['POST', 'GET'])
def account_settings():
    if 'session' not in request.cookies.keys():
        return render_template('login.html')
    else:
        token = request.cookies['session']
        result, new_token = server.login_token(token)
        if result:
            response = make_response(render_template('account_setting.html'))
            response.set_cookie('session', new_token)
            response.set_cookie('account_type', server.get_permission(new_token))
            return response
        else:
            return render_template('login.html')


@app.route('/buck_upload', methods=['POST', 'GET'])
def bulkapi():
    if not session.get('logged_in'):
        return redirect('/')
    files = request.files
    form = request.form
    file = files.get('buck_questions')
    file.save("uploads/upload1.docx")
    info, string = examdb.docs.parse_doc("uploads/upload1.docx", 1)
    # output_file = ""
    # with open("templates/upload_result.html", "r") as f:
    #     for i in f:
    #         output_file += i
    #     output_file = output_file.replace("{{data}}", string)
    # with open("templates/test_result.html", "w", encoding='utf-8') as f:
    #     f.write(output_file)
    examdb.app.bulk_add(info)
    return render_template("upload_result.html", data=string)


@app.route('/query', methods=['POST', 'GET'])
def query():
    if not session.get('logged_in'):
        return redirect('/')
    pass


if __name__ == '__main__':
    server = examdb.server.Server()
    app.run(host='localhost', port=5000)
