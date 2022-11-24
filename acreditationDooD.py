import os
import datetime

import shutil
# import qrcode

from shutil import ignore_patterns
# import qrcode.image.svg




def count(dir, counter=0):
    pout = open('out.txt', 'w')
    "returns number of files in dir and subdirs"
    for pack in os.walk(dir):
        for f in pack[2]:
            pout.write(str(dir) +str(pack[0])+ str(f) +'\n' )
            counter += 1
    pout.close()
    return dir + " : " + str(counter) + "files"
# вывод списка файлов в папке
def dirFolder():
    dir = "M:/"
    # dir = "d:/s_hare"
    report = "D:\\report/report.txt"
    # report = "M://"
    # p = os.listdir(dir)
    # for i in p:
    #     print(i)
    with open(report, "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(dir):
            filewrite.write(r+'\n')
            for i in f:
                filewrite.write(i+'\n')
    filewrite.close()


# пробегает по директории и создает файл с рестром папок с пометкой пуста папка или нет
def compil_ot_file(dirName,fileOutName):
    dirName1 = 'O:\\01 ОПОП/АРХИВ/БАЗА УП НА АККРЕДИТАЦИЮ/'
    # dirName = 'D:\\up base'

    # listName = ['аОПОП', 'аРПУД', 'прил 0 опоп', 'прил 1 КУГ', 'прил 2 УП', 'прил 3 МК','прил 4 РПУДы','прил 5 ПП НИР',
    #             'прил 6 пр ГИА','прил 7 ССК','прил 8 ЭБС','прил 9 МТО','прил 10 РОП','ЭУК']

    listName = ['аОПОП', 'аРПД', 'опоп', 'УП', 'Метод и иные документы','РПУД', 'ПП НИР', 'ГИА', 'ФОС', 'ДОГОВОР',
     'Воспитательная работа', 'КИМ']

    numb = 0
    numberPapok = 0

    bufSTR ="1"
    bufSTR2 = '2'

    fileOut = dirName1 + '\Struct\\'+fileOutName
    print(fileOut)
    with open(fileOut, "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(dirName):
            for i in listName:
                # if(i in str(r)):
                if(str(r).endswith(i)):
                    # отрезает корень каталога из начала строки , Добавляет в конец имя нужной папки через ;
                    # r1 = r.replace(';','')
                    b = r[dirName.__len__():str(r).rfind(str(i))]+';'+str(i)
                    # print(b)
                    bufSTR = b + ';' + ' 0' + '\n'

                    # bufSTR = str(r)+'/'+ '0' +'\n'
                    filewrite.write(bufSTR)
                    for file in f:
                        # print(str(r)+'/'+str(file) +'\n')
                        # Исключаем скрытый системный файл , вопрос почему переодически крашится от вывода на печать имя фйлов
                        if((str(file)!='Thumbs.db') and (str(file).endswith('.pdf') or (str(file).endswith('.docx')))):
                            # r1 = r.replace(';','')
                            # отрезает корень каталога из начала строки , Добавляет в конец имя нужной папки через ;
                            b = r[dirName.__len__():str(r).rfind(str(i))]+';'+str(i)
                            bufSTR = b + ';' + ' 1' + '\n'

                            if(bufSTR != bufSTR2):
                                filewrite.write(bufSTR)
                                numberPapok += 1
                                bufSTR2 = bufSTR
            numb += 1
            print("пройдено = " + str(numb) + ' найдено папок = '+str(numberPapok))
        print('ххх',numb,listName)
        print(dirName)
    print('процент заполнения = ' + str(100*numberPapok/numb)[0:4] + '%')

    # запись логов обновления
    logupdate = open(dirName1 + '\Struct\\'+'logupdate.txt','a')
    run = datetime.datetime.today()
    logupdate.write(str(run.__format__('%d-%m-%Y %H:%M:%S'))+';'+str(numb)+';'+ str(numberPapok)+';'+str(100*numberPapok/numb)[0:4]+'\n')
    logupdate.close()



    fout = open(dirName1 + '\Struct\\' + 'src.txt', 'w')
    fout.write(datetime.datetime.today().strftime("%d/%m/%Y:%H-%M-%S"))
    fout.close()

# Создание QR кода
def qrcodeprint():
    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    # The data that you want to store
    data = "https://www.dvfu.ru/about/rectorate/4915/the-department-of-organization-of-educational-activities/"
    probel = "\n"
    name = "Департамент организации образовательной деятельсти , - За подмену листа, убью сука!"
    # Add data
    qr.add_data(data)
    qr.add_data(probel)
    qr.add_data(name)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("image.jpg")

#копирует директорию с pdf
def copy_to_pdf(directory,directoryToPdf,school):
    print(school)
    listName = ['*аОПОП*','*аРПУД*','*прил 0 опоп*','*прил 1 КУГ*','*прил 2 УП*','*прил 3 МК*','*прил 4 РПУДы*','*прил 5 ПП НИР*',
                '*прил 6 пр ГИА*','*прил 7 ССК*','*прил 8 ЭБС*','*прил 9 МТО*','*прил 10 РОП*','*ЭУК*']
    # рабочая схема
    shutil.copytree(directory+school,directoryToPdf+'/'+school,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm','*.db',
                                                                    '*.xlsx','*.doc','*.xls','*.xlsm','*.rtf','*Арсеньев*',
                                                                    '*аспирантура*','*Большой Камень*','*Дальнегорск*',
                                                                    '*Находка*','*Уссурийск*','*ЦРПДО*',
                                                                    '*Электронные версии ОС ВО ДВФУ*',
                                                                    '*Электронные версии ФГОС ВО*',
                                                                    '*Электронные версии ФГОС ВО 3++*','*УВЦ*',
                                                                    '*российско-австралийская*','*российско-американская*',
                                                                    '*е выходя*','*Б1.Б.1_Философские проблемы науки и техники-1-2.pdf*',
                                                                    '*Б1.Б.5_Общая теория динамических систем1-1-2*',
                                                                    '*аОПОП*','*аРПУД*','*прил 0 опоп*','*прил 1 КУГ*',
                                                                    '*прил 3 МК*','*прил 4 РПУДы*','*прил 5 ПП НИР*',
                                                                    '*прил 6 пр ГИА*','*прил 7 ССК*','*прил 8 ЭБС*','*прил 9 МТО*','*прил 10 РОП*','Договора','*ЭУК*'))
    # shutil.copytree(directory+school,directoryToPdf+'/'+school,ignore=ignore_patterns('*.*' )  )
    print("Закопировано")


# выполняет задание по обновлению
def updateQuest(dirName):
    print("updateQuest")

    dirToPDF = 'D:\\up base PDF\\UPDATE'
    # dir1 = "O:\\БАЗА УП НА АККРЕДИТАЦИЮ"
    dir1 = 'O:\\БАЗА ОПОП на 2020-2021 уч.г'
    fileQuest = "ОБНОВЛЕНИЕ.txt"

    logUpdate = open('D:\\up base PDF\\logUpdate.txt', 'a')
    f = open(dir1+'\\'+fileQuest,'r')
    print(dir1+'\\'+fileQuest)

    print("Блокнот \n")
    # dirName1="M:\БАЗА ОПОП 2020 г.н/"
    # print(dirName1)
    # print(dirName1[0:len(dirName)-1:1])

    for line in f:
        print(line)
    # shutil.copy(dir1+fileQuest,r'D:/1.txt')
        str1 = 'M'+line[1:]
        str1 = str1.replace('\n','')
        # S[i:j:step]

        # str2 = str1.replace(dirName[0:len(dirName)-1:1], dirToPDF) #'M:\\БАЗА ОПОП на 2019-2020 уч.г'    "M:\БАЗА ОПОП 2020 г.н"
        str2 = str1.replace(str1[0:len("M:\БАЗА ОПОП на 2020-2021 уч.г")], dirToPDF) #'M:\\БАЗА ОПОП на 2019-2020 уч.г'    "M:\БАЗА ОПОП 2020 г.н"


        print(str1)
        print(str2)

        run = datetime.datetime.today()
        logUpdate.write(str(run.__format__('%d-%m-%Y %H:%M:%S'))+' ' + str2+'\n')

        shutil.copytree(str1,str2,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm','*.db',
                                                                                          '*.xlsx','*.doc','*.xls','*.xlsm','*.rtf','*Арсеньев*',
                                                                                          '*аспирантура*','*Большой Камень*','*Дальнегорск*',
                                                                                          '*Находка*','*Уссурийск*','*ЦРПДО*',
                                                                                          '*Электронные версии ОС ВО ДВФУ*',
                                                                                          '*Электронные версии ФГОС ВО*',
                                                                                          '*Электронные версии ФГОС ВО 3++*','*УВЦ*',
                                                                                          '*российско-австралийская*','*российско-американская*',
                                                                                          '*е выходя*'))
        # shutil.copytree(str1,str2,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm','*.db',
        #                                                  '*.xlsx','*.doc','*.xls','*.xlsm','*.rtf','*Арсеньев*',
        #                                                  '*аспирантура*','*Большой Камень*','*Дальнегорск*',
        #                                                  '*Находка*','*Уссурийск*','*ЦРПДО*',
        #                                                  '*Электронные версии ОС ВО ДВФУ*',
        #                                                  '*Электронные версии ФГОС ВО*',
        #                                                  '*Электронные версии ФГОС ВО 3++*','*УВЦ*',
        #                                                  '*российско-австралийская*','*российско-американская*',
        #                                                  '*е выходя*'))



    logUpdate.close()


# main функция
def accreditationCopy():
    dirName = 'M:\\БАЗА ОПОП на 2019-2020 уч.г/'
    # dirName ='N:\\АККРЕДИТАЦИЯ/БАЗА ОПОП на 2020-2021 уч.г/'
    # dirName = 'D:\\up base'
    # dirToPDF = 'D:\\up base PDF'
    dirToPDF = 'W:\\Осеев Е.Е/up base PDF'

    # fileOutAll = 'file.txt'
    # fileOutPDF = 'filePDF.txt'

    SCHOOL = ['ВИ-ШРМИ','ИШ','ШБМ','ШЕН','ШИГН','ШЦЭ','ШЭМ','ЮШ','филиал в г. Арсеньеве',
              'филиал в г. Находке','филиал в г. Уссурийске (ШП)']


    # копирует пдфки
    for i in SCHOOL:
        copy_to_pdf(dirName,dirToPDF,i)


def accreditation():
    # dirName ='M:\\АККРЕДИТАЦИЯ/БАЗА ОПОП на 2022-2023 уч.г/TEST/'
    dirName ='M:\\БАЗА ОПОП на 2022-2023 уч.г\TEST'

    dirToPDF = 'D:\\up base PDF'
    # dirToPDF = 'W:\\Осеев Е.Е/up base PDF'

    fileOutAll = 'file.txt'
    fileOutPDF = 'filePDF.txt'

    # SCHOOL = ['ВИ-ШРМИ','ИШ','ШБМ','ШЕН','ШИГН','ШЦЭ','ШЭМ','ЮШ','ШП','филиал в г. Арсеньеве',
    #           'филиал в г. Находке','филиал в г. Уссурийске (ШП)']

    SCHOOL = ['ВИ-ШРМИ','ИМиКТ','ИМО','ИНЖБМ','ИНТиПМ','ПИШ Текутьева','Политех','ф.Арсеньев','ШИГН','ШМ','ШП',
              'ШЭМ','ЮШ']

    # Создать общий выходной файл ГЛАВНЫЙ ПОДСЧЕТ ДЛЯ ТАБЛИЦ
    compil_ot_file(dirName,fileOutAll)

    # Создать выходной файл для PDF директории
    # compil_ot_file(dirToPDF, fileOutPDF)

    # qrcodeprint()

    # копирует пдфки
    # copyUGPI()
    # for i in SCHOOL:
    #     copy_to_pdf(dirName,dirToPDF,i)

    # Копирует ОПЫ ОПЫ
    # for i in SCHOOL:
    #     copy_to_pdfOPOP(dirName,dirToPDF_OPOP,i)
    # findPDFTEST(pathtest=dirToPDF)
    #

    # copy_to_pdf(dirName,dirToPDF,'ШИГН') #ШИГН1
    # copy_to_pdf(dirName,dirToPDF,'ЮШ') #ЮШ
    # copy_to_pdf(dirName,dirToPDF,'ШЕН/Магистратура')
    # copy_to_pdf(dirName,dirToPDF,'ИШ')
    # copy_to_pdf(dirName,dirToPDF,'ВИ-ШРМИ')

    # обновление по запросу
    # updateQuest(dirName)
