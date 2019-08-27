from flask import *
import examdb.app
import traceback
import examdb.docs
from datetime import timedelta
import os
app = Flask(__name__)


@app.before_request
def session_life_time():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/', methods=['POST', 'GET'])
def login():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect('/dashboard')


@app.route('/authen', methods=['POST'])
def authenticate():
    form = request.form
    print(form)
    username = form.get('uname')
    password = form.get('psw')
    result, code = examdb.app.authenticate(username, password)
    if result:
        session['logged_in'] = True
        return redirect('/dashboard')
    else:
        if code == 0:
            flash('No such username')
            return redirect('/')
        if code == 1:
            flash('Wrong password')
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
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('my_dashboard.html', search_results={})


@app.route('/buck_upload', methods=['POST', 'GET'])
def bulkapi():
    if not session.get('logged_in'):
        return redirect('/')
    files = request.files
    form = request.form
    print(files)
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
    app.secret_key = os.urandom(12)
    app.run(host='localhost', port=5000)
