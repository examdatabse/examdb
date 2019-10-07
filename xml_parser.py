import xmltodict


def parse_correct_answer(docname):
    f = open("document.xml", encoding='utf-8')
    xmlstr = ''
    for i in f:
        xmlstr += i
    d = xmltodict.parse(xmlstr)
    c = 0
    ans = []
    # questions = []
    for j, i in enumerate(d['w:document']['w:body']['w:p']):
        if 'w:r' in i.keys():
            if isinstance(i['w:r'], xmltodict.OrderedDict):
                if isinstance(i['w:r']['w:t'], xmltodict.OrderedDict):
                    if '#text' in i['w:r']['w:t'].keys():
                        # print(j)
                        c += 1
                        if 'w:color' in i['w:pPr']['w:rPr'].keys():
                            if i['w:pPr']['w:rPr']['w:color']['@w:val'] == 'FF0000':
                                ans.append(c - 1)
                                # print(i['w:pPr']['w:rPr']['w:color'])
                        # print("dict", i['w:r']['w:t']['#text'])
                        # questions.append(i['w:r']['w:t']['#text'])
                elif isinstance(i['w:r']['w:t'], str):
                    # print(j)
                    c += 1
                    if 'w:color' in i['w:pPr']['w:rPr'].keys():
                        if i['w:pPr']['w:rPr']['w:color']['@w:val'] == 'FF0000':
                            ans.append(c - 1)
                            # print(i['w:pPr']['w:rPr']['w:color'])
                    # print("dict", i['w:r']['w:t'])
                    # questions.append(i['w:r']['w:t'])
            elif isinstance(i['w:r'], list):
                first = True
                # q_str = ''
                for k in i['w:r']:
                    if 'w:t' in k.keys():
                        if isinstance(k['w:t'], str):
                            if first:
                                # print(j)
                                if 'w:color' in i['w:pPr']['w:rPr'].keys():
                                    if i['w:pPr']['w:rPr']['w:color']['@w:val'] == 'FF0000':
                                        ans.append(c)
                                        # print(i['w:pPr']['w:rPr']['w:color'])
                                c += 1
                                first = False
                            # print("list ", k['w:t'])
                            # q_str += k['w:t'] + ' '
                        else:
                            if '#text' in k['w:t'].keys():
                                if first:
                                    # print(j)
                                    if 'w:color' in i['w:pPr']['w:rPr'].keys():
                                        if i['w:pPr']['w:rPr']['w:color']['@w:val'] == 'FF0000':
                                            ans.append(c)
                                            # print(i['w:pPr']['w:rPr']['w:color'])
                                    c += 1
                                    first = False
                                # print("list ", k['w:t']['#text'])
                                # q_str += k['w:t']['#text']
                        # print("list", type(k['w:t']))
                # if q_str != '':
                    # questions.append(q_str)
    return ans


def assign_answer(ans):
    data = dict()
    for i in ans:
        data[i // 6] = i % 6
    return data


def print_result(ans):
    choice_map = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E'
    }
    for i in ans.keys():
        print(i + 1, choice_map[ans[i]])


if __name__ == '__main__':
    answers = parse_correct_answer('document.xml')
    mapped_answers = assign_answer(answers)
    print_result(mapped_answers)
