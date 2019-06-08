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
    print(form)
    print(files)
    q_code = form['q-code']
    permission = form['permission']
    question = form['question']
    choice1 = form['choice1']
    choice2 = form['choice2']
    choice3 = form['choice3']
    choice4 = form['choice4']
    choice5 = form['choice5']
    choice1_img = files.get('choice_image1')
    choice2_img = files.get('choice_image2')
    choice3_img = files.get('choice_image3')
    choice4_img = files.get('choice_image4')
    choice5_img = files.get('choice_image5')
    print(type(choice1))
    answerfile = files.get('answer')
    question_img = files.get('question_image')
    if choice1 == '' or choice2 == '' or choice3 == '' or choice4 == '' or choice5 == '' or q_code == '' \
            or question == '' or permission == '':
        raise Exception('Required fields empty')
    if choice1_img is None:
        choice1_img = bytes('', 'utf-8')
    else:
        choice1_img = choice1_img.read()
    if choice2_img is None:
        choice2_img = bytes('', 'utf-8')
    else:
        choice2_img = choice2_img.read()
    if choice3_img is None:
        choice3_img = bytes('', 'utf-8')
    else:
        choice3_img = choice3_img.read()
    if choice4_img is None:
        choice4_img = bytes('', 'utf-8')
    else:
        choice4_img = choice4_img.read()
    if choice5_img is None:
        choice5_img = bytes('', 'utf-8')
    else:
        choice5_img = choice5_img.read()
    if answerfile is None:
        answerfile = bytes('', 'utf-8')
    else:
        answerfile = answerfile.read()
    if question_img is None:
        question_img = bytes('', 'utf-8')
    else:
        question_img = question_img.read()
    Problems.create(serial_code=q_code, permission=permission, question=question, choice1=choice1,
                    choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, timestamp=time.time(),
                    answer_image_a=choice1_img, answer_image_b=choice2_img, answer_image_c=choice3_img,
                    answer_image_d=choice4_img, answer_image_e=choice5_img, question_image=question_img)
