import pypandoc
from bs4 import BeautifulSoup
import re


def parse_doc(docname, offset):
    output = pypandoc.convert_file(docname, 'html', extra_args=['--extract-media=static/exam_imgs/{}'.format(offset)])
    soup = BeautifulSoup(output, "html.parser")
    all_questions = soup.find_all(["p", "table"])
    all_questions = list(all_questions)
    i = 0
    question_info = dict()
    curr_code = ""
    while i < len(all_questions):
        j = all_questions[i]
        portion = j.text[1:len(j.text)].split(":")
        if portion[0] == "QCode":
            portion[1] = portion[1].replace("{", "")
            portion[1] = portion[1].replace("}", "")
            curr_code = portion[1]
            question_info[curr_code] = dict()
            # print("Question Number:", portion[1])

        if portion[0] == "Serial":
            portion[1] = portion[1].replace("{", "")
            portion[1] = portion[1].replace("}", "")
            question_info[curr_code]["serial"] = portion[1]
            # print("Serial Number:", portion[1])

        if portion[0] == "Permission":
            portion[1] = portion[1].replace("{", "")
            portion[1] = portion[1].replace("}", "")
            question_info[curr_code]["permission"] = portion[1]
            # print("Permission:", portion[1])

        if portion[0] == "Ans":
            portion[1] = portion[1].replace("{", "")
            portion[1] = portion[1].replace("}", "")
            question_info[curr_code]["ans"] = portion[1]
            # print("Answer:", portion[1])

        if portion[0] == "Question":
            question_body = str(j).replace("@Question:", "")
            if question_body.find("{") != -1 and question_body.find("}") == -1:
                long_question = ""
                while True:
                    content = str(all_questions[i])
                    long_question += content + "\n"
                    if content.find("}") != -1:
                        break
                    i += 1
                question_body = long_question
            question_body = question_body.replace("@Question:", "")
            question_body = question_body.replace("{", "")
            question_body = question_body.replace("}", "")
            question_info[curr_code]["qbody"] = question_body
            # print("Question Body:\n", question_body)

        if portion[0] == "Choice1":
            choice = str(j).replace("@Choice1:", "")
            choice = choice.replace("{", "")
            choice = choice.replace("}", "")
            question_info[curr_code]["c1"] = choice
            # print("Choice1", choice)

        if portion[0] == "Choice2":
            choice = str(j).replace("@Choice2:", "")
            choice = choice.replace("{", "")
            choice = choice.replace("}", "")
            question_info[curr_code]["c2"] = choice
            # print("Choice2", choice)

        if portion[0] == "Choice3":
            choice = str(j).replace("@Choice3:", "")
            choice = choice.replace("{", "")
            choice = choice.replace("}", "")
            question_info[curr_code]["c3"] = choice
            # print("Choice3", choice)

        if portion[0] == "Choice4":
            choice = str(j).replace("@Choice4:", "")
            choice = choice.replace("{", "")
            choice = choice.replace("}", "")
            question_info[curr_code]["c4"] = choice
            # print("Choice4", choice)

        if portion[0] == "Choice5":
            choice = str(j).replace("@Choice5:", "")
            choice = choice.replace("{", "")
            choice = choice.replace("}", "")
            question_info[curr_code]["c5"] = choice
            # print("Choice5", choice)

        # print(j)
        i += 1

    return question_info, output


if __name__ == '__main__':
    print(parse_doc("test.docx", 3))
    # with open("test1.html", 'r') s f:
    #     for i in f:
    #         print(i)

