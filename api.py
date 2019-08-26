from flask import *
import examdb.app
import traceback
import examdb.docs
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def get_form_data():
    return render_template('add_question.html')


@app.route('/add', methods=['POST', "GET"])
def add():
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
    return render_template('my_dashboard.html', search_results={})


@app.route('/buck_upload', methods=['POST', 'GET'])
def bulkapi():
    files = request.files
    form = request.form
    print(files)
    file = files.get('buck_questions')
    file.save("uploads/upload1.docx")
    info, string = examdb.docs.parse_doc("uploads/upload1.docx", 1)
    output_file = ""
    with open("templates/upload_result.html", "r") as f:
        for i in f:
            output_file += i
        output_file = output_file.replace("{{data}}", string)
    with open("templates/test_result.html", "w", encoding='utf-8') as f:
        f.write(output_file)
    return render_template("test_result.html")


@app.route('/query', methods=['POST', 'GET'])
def query():
    pass


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
