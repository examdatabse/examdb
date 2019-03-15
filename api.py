from flask import *
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def get_form_data():
    page = open('add_question.html', encoding='utf-8')
    res = page.read()
    return res


@app.route('/add', methods=['POST', "GET"])
def add():
    return "Added"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
