# This is a sample Python script.

import csv
import json
import os
import re

def make_struct(dist="plan1.csv"):
    """читает csv"""

    list_dist = ['аОПОП', 'аРПД', 'опоп', 'УП', 'Метод и иные документы','РПУД', 'ПП НИР', 'ГИА', 'ФОС', 'ДОГОВОР',
                 'Воспитательная работа', 'КИМ']
    lvl_str = {
        '03': "бакалавриат",
        '04': "магистратура",
        '05': "специалитет",
        '08': "ординатура",
    }
    form_str = {
        'очная': '',
        'заочная': 'ЗФО',
        'заочная (с применением дистанционных образовательных технологий)': 'ЗФО ДОТ'
    }


    jsonfile = open('file.json', 'w')
    # with open(dist, newline='', encoding="utf-8") as csvfile:
    with open(dist, newline='', encoding="windows-1251") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if row['Образовательная программа/специализация']:
                print(row['Образовательная программа/специализация'])
                op = row['Образовательная программа/специализация'].replace("/","").replace('"', ''). \
                    replace(":", '').replace("\n","")
                print(re.split("\)|\(|-| ", op.replace('(', '').replace(')', '')))
                res = [x for x in re.split("\)|\(|-| ", op.replace('(', '').replace(')', '')) if x is not None]
                print(res)
            else:
                # op = "no program"
                op = row['Направление/специальность'][9:]
            for i in list_dist:
                str_dist = row['Наименование школы']+"/" + lvl_str[row['Направление/специальность'][3:5]]+"/" + \
                           row['Год набора']+" г.н. " + form_str[row['Форма обучения']]+" " + \
                           row['Направление/специальность'][:8]+" " + op + '/' + i
                print(str_dist.replace("  ", " "))
                # dist = "C:\\Users\oseev.ee\PycharmProjects\dood 1.0\\test1\\" + str_dist.replace("  ", " ")
                dist = "D:\\struct\\" + str_dist.replace("  ", " ")
                print(len(dist))
                # dist = "C:\\Users\\007\PycharmProjects\DOOD\\test1\\" + str_dist.replace("  ", " ")
                if os.path.exists(dist):
                    print("true")
                else:
                    os.makedirs(dist)
                    print("false")

            # Форма обучения
            # Направление/специальность
            # Образовательная программа/специализация

            # print(row)
            # print(json.dumps(row))
            # json.dump(row, jsonfile)
            # jsonfile.write(',\n')
            # t = json.dumps(row)
    print("sdfsfsg")

    # print(t)
    # k = json.loads(t)
    # for i in k.keys():
    #     print(i,'   ->', k[i])
    # print(k['id'])

