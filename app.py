import time

from examdb.databse import Users


import time
import pickle
from examdb.databse import Problems
from examdb.cache import Cache


class QueryResult:
    _id = 0
    _serial_code = ''
    _tags = []
    _question = ''
    _image = ''
    _answer = ''
    _ans_images = {}
    _ans_choices = {}
    _time_stamp = 0

    def __init__(self, id, serial, tags, question, img, ans, ans_imgs, ans_choices, time):
        self._id = id
        self._serial_code = serial
        self._tags = tags
        self._question = question
        self._image = img
        self._answer = ans
        self._ans_images = ans_imgs
        self._ans_choices = ans_choices
        self._time_stamp = time
        pass


class QueryQuestion:

    _id_cache = Cache()
    _tags_cache = Cache()

    def __init__(self):
        pass

    def query(self, method, parameters):
        if method == '0':
            self.query_by_id(parameters)
        elif method == '1':
            self.query_by_tags(parameters)
        else:
            self.query_by_keywords(parameters)

    def query_by_id(self, id):
        if self._id_cache.contain(id):
            return
        query = Problems.select().where(Problems.id == id)
        if len(query) == 0:
            return False, ''
        else:
            for q in query:
                return True, {
                    'id': q.id,
                    'serial': q.serial_code,
                    'tags': q.tags,
                    'testlet': q.question,
                    'permission': q.permission,
                    'question_image': q.question_image,
                    'answer': q.answer,
                    'ans_image1': q.answer_image_a,
                    'ans_image2': q.answer_image_b,
                    'ans_image3': q.answer_image_c,
                    'ans_image4': q.answer_image_d,
                    'ans_image5': q.answer_image_e,
                    'choice1': q.choice_1,
                    'choice2': q.choice_2,
                    'choice3': q.choice_3,
                    'choice4': q.choice_4,
                    'choice5': q.choice_5,
                    'time': time
                }

    def query_by_tags(self, tag):
        query = Problems.select().where(True)
        result = list()
        for q in query:
            tags = set(q.tags.split('&'))
            if tag in tags:
                result.append({
                    'id': q.id,
                    'serial': q.serial_code,
                    'tags': q.tags,
                    'testlet': q.question,
                    'permission': q.permission,
                    'question_image': q.question_image,
                    'answer': q.answer,
                    'ans_image1': q.answer_image_a,
                    'ans_image2': q.answer_image_b,
                    'ans_image3': q.answer_image_c,
                    'ans_image4': q.answer_image_d,
                    'ans_image5': q.answer_image_e,
                    'choice1': q.choice_1,
                    'choice2': q.choice_2,
                    'choice3': q.choice_3,
                    'choice4': q.choice_4,
                    'choice5': q.choice_5,
                    'time': time
                })

    def query_by_keywords(self, tags):
        pass


def add_questions(form, files):
    choices = form.getlist('choice')
    choice_images = files.getlist('choice_image')
    for i in range(5 - len(choices)):
        choices.append('')
    for i in range(5 - len(choice_images)):
        choice_images.append('')
    for i in range(5):
        choice_images[i] = pickle.dumps(choice_images[i])

    Problems.create(serial_code=form['q-code'], permission=form['permission'], question=form['question'],
                    choice_1=choices[0], choice_2=choices[1], choice_3=choices[2], choice_4=choices[3], choice_5=
                    choices[4], answer_image_a=choice_images[0], answer_image_b=choice_images[1], answer_image_c=
                    choice_images[2], answer_image_d=choice_images[3], answer_image_e=choice_images[4],
                    time=time.time()
                    )
    pass


def bulk_add(bulk):
    for i in bulk.keys():
        question = bulk[i]
        Problems.create(serial_code=question['serial'], permission=question['permission'],
                        question=question['qbody'], choice_1=question['c1'], choice_2=question['c2'],
                        choice_3=question['c3'], choice_4=question['c4'], choice_5=question['c5'],
                        time=time.time(), answer=question['ans']
                        )


def authenticate(username, password):
    query = Users.select().where(Users.username == username)
    pw = ''
    for i in query:
        pw = i.password
    if pw == '':
        return False, 0
    elif pw != password:
        return False, 1
    else:
        return True, 2


def load_info():
    query = Users.select().where(True)
    login_info = dict()
    for i in query:
        login_info[i.username] = {'password': i.password, 'permission': i.permission, 'first_name': i.first_name,
                              'last_name': i.last_name}
    return login_info

