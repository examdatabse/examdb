import time

from databse import Users


import time
import pickle
from databse import Problems
from cache import Cache


class DatabaseManager:

    def __init__(self):
        pass

    @staticmethod
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
                        time_stamp=time.time()
                        )

    @staticmethod
    def bulk_add(bulk):
        for i in bulk.keys():
            question = bulk[i]
            Problems.create(serial_code=question['serial'], permission=question['permission'],
                            question=question['qbody'], choice_1=question['c1'], choice_2=question['c2'],
                            choice_3=question['c3'], choice_4=question['c4'], choice_5=question['c5'],
                            time_stamp=time.time(), answer=question['ans']
                            )

    @staticmethod
    def load_info():
        query = Users.select().where(True)
        login_info = dict()
        for i in query:
            login_info[i.username] = {'password': i.password, 'permission': i.permission, 'first_name': i.first_name,
                                      'last_name': i.last_name}
        return login_info

