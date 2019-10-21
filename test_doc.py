import pypandoc
from bs4 import BeautifulSoup
import re
import csv
import xml_parser


def parse_doc(docname, offset):
    output = pypandoc.convert_file(docname, 'html', extra_args=['--extract-media=static/exam_imgs/{}'.format(offset)])
    result = re.findall("@Begin.*?@QCode:{(.*?)}.*?@Serial:{(.*?)}.*?@Permission:{(.*?)}.*?@Ans:{(.*?)}.*?"
                        "@Question:{(.*?)}.*?@Choice1:{(.*?)}.*?@Choice2:{(.*?)}.*?@Choice3:{(.*?)}.*?@Choice4:{(.*?)}."
                        "*?@Choice5:{(.*?)}.*?@End", output, re.S)
    questions = dict()
    for i, j in enumerate(result):
        # print(i + 1)
        # print()
        questions[j[0]] = dict()
        questions[j[0]]['serial'] = j[1]
        questions[j[0]]['permission'] = j[2]
        questions[j[0]]['ans'] = j[3]
        questions[j[0]]['qbody'] = j[4]
        questions[j[0]]['c1'] = j[5]
        questions[j[0]]['c2'] = j[6]
        questions[j[0]]['c3'] = j[7]
        questions[j[0]]['c4'] = j[8]
        questions[j[0]]['c5'] = j[9]
        # for k in j:
        #     k = k.strip()
        #     print(k, end=" ")
        # print()
    print(questions)
    # file = open('t2.html', 'w', encoding='utf-8')
    # soup = BeautifulSoup(output, "html.parser")
    # file.write(soup.prettify())
    return output


def parse_doc_unformatted(docname, offset, attr_data, answer_file):
    output = pypandoc.convert_file(docname, 'html', extra_args=['--extract-media=static/exam_imgs/{}'.format(offset)])
    # file = open('t2.html', 'w', encoding='utf-8')
    soup = BeautifulSoup(output, "html.parser")
    # file.write(soup.prettify())
    result = re.findall("<li>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>"
                        ".*?<p>(.*?)</p>.*?</li>", output, re.S)
    questions = dict()
    answers = xml_parser.assign_answer(xml_parser.parse_correct_answer(answer_file))
    choice_map = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E'
    }
    for i, j in enumerate(result):
        questions[attr_data[i]['qcode']] = dict()
        questions[attr_data[i]['qcode']]['serial'] = attr_data[i]['serial'].strip()
        questions[attr_data[i]['qcode']]['permission'] = attr_data[i]['permission'].strip()
        questions[attr_data[i]['qcode']]['ans'] = choice_map[answers[i]].strip()
        questions[attr_data[i]['qcode']]['qbody'] = j[0].strip()
        questions[attr_data[i]['qcode']]['c1'] = j[1].strip()
        questions[attr_data[i]['qcode']]['c2'] = j[2].strip()
        questions[attr_data[i]['qcode']]['c3'] = j[3].strip()
        questions[attr_data[i]['qcode']]['c4'] = j[4].strip()
        questions[attr_data[i]['qcode']]['c5'] = j[5].strip()
        # print(i + 1)
        # print(j)
    return questions


def parse_csv(attr_file):
    file = open(attr_file, encoding='utf-8')
    readcsv = csv.reader(file, delimiter=',')
    data = dict()
    for j, i in enumerate(readcsv):
        if j != 0:
            data[j - 1] = dict()
            data[j - 1]['qcode'] = i[0]
            data[j - 1]['serial'] = i[1]
            data[j - 1]['permission'] = i[2]
    # print(data)
    return data


if __name__ == '__main__':
    # parse_doc_unformatted('test2.docx', 10, parse_csv('test.csv'), 'document.xml')
    parse_doc('test.docx', 11)
    # pat = re.compile("^<ol>.*?</ol>$")
    # result = re.findall("<li>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>"
    #                     ".*?<p>(.*?)</p>.*?</li>", test, re.S)
    # print()
    # print()
    # for i, j in enumerate(result):
    #     print(i + 1)
    #     print(len(j))
    #     print(j)
    # test = parse_doc('test.docx', 11)
    # result = re.findall("@Begin.*?@QCode:{(.*?)}.*?@Serial:{(.*?)}.*?@Permission:{(.*?)}.*?@Ans:{(.*?)}.*?"
    #                     "@Question:{(.*?)}.*?@Choice1:{(.*?)}.*?@Choice2:{(.*?)}.*?@Choice3:{(.*?)}.*?@Choice4:{(.*?)}."
    #                     "*?@Choice5:{(.*?)}.*?@End", test, re.S)
    # # print(test)
    # # result = re.findall("@Begin(.*?)@End", test, re.S)
    # # print(result)
    # for i, j in enumerate(result):
    #     print(i + 1)
    #     print()
    #     for k in j:
    #         k = k.strip()
    #         print(k, end=" ")
    #     print()
    pass
