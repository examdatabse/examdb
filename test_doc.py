import pypandoc
from bs4 import BeautifulSoup
import re


def parse_doc(docname, offset):
    output = pypandoc.convert_file(docname, 'html', extra_args=['--extract-media=static/exam_imgs/{}'.format(offset)])
    file = open('t2.html', 'w', encoding='utf-8')
    soup = BeautifulSoup(output, "html.parser")
    file.write(soup.prettify())
    return output


def parse_doc_unformatted(docname, offset):
    output = pypandoc.convert_file(docname, 'html', extra_args=['--extract-media=static/exam_imgs/{}'.format(offset)])
    file = open('t2.html', 'w', encoding='utf-8')
    soup = BeautifulSoup(output, "html.parser")
    file.write(soup.prettify())
    result = re.findall("<li>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>"
                        ".*?<p>(.*?)</p>.*?</li>", output, re.S)
    for i, j in enumerate(result):
        print(i + 1)
        print(j)


if __name__ == '__main__':
    parse_doc_unformatted('test2.docx', 10)
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
