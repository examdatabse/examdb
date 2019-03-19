
import time

from examdb.databse import Problems


def query_question(id):
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


def add_questions(form, files):
    pass
