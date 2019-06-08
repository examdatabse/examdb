from flask import *
import examdb.app
import traceback
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def get_form_data():
    return render_template('add_question.html')


@app.route('/add', methods=['POST', "GET"])
def add():
    files = request.files
    form = request.form
    try:
        examdb.app.add_questions(form, files)
    except Exception:
        traceback.print_exc()
    return "Added"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
