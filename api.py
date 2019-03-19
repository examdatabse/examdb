from flask import *
import examdb.app
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def get_form_data():
    return render_template('add_question.html')


@app.route('/add', methods=['POST', "GET"])
def add():
    # q_code = request.form['question_image']
    # print(len(q_code))
    for i in request.files:
        print(i)
    return "Added"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
