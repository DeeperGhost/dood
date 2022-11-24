import os, datetime
import pathlib

import shutil


def scaner():
    # dir = "D://1cTandem\рабочая папка//22"
    dir = "M:\БАЗА ОПОП на 2022-2023 уч.г"
    reportFile = "fileTest.csv"
    # dir = "N:\АККРЕДИТАЦИЯ\БАЗА ОПОП на 2022-2023 уч.г"
    i = 0

    with open(reportFile, "w", encoding="utf-8") as filewrite:
        filewrite.write(".file; size; modif; create; open;numberID;filename;disk; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10;\n")
        for r, d, f in os.walk(dir):
            print(str(i)+"\n")
            print("r=", r, "\n", "d=", d, "\n", "f=", f, "\n")
            for j in f:
                try:
                    file = r+"/"+j
                    print("f=", file)
                    node = file.replace("//", "\\").replace("/", "\\").split("\\")
                    # print((r+j).replace("\\","/").split("/"), "\n")
                    print((r+j).replace("//", "\\").replace("/", "\\").split("\\"), "\n")


                    print("расширение=", pathlib.Path(file).suffix)
                    print("стата=", pathlib.Path(file).lstat())

                    statFile = pathlib.Path(file).lstat()

                    print("размер=", statFile.st_size/1024)
                    print("изменен=", datetime.datetime.fromtimestamp(statFile.st_mtime))
                    print("создан=", datetime.datetime.fromtimestamp(statFile.st_ctime))
                    print("открыт=", datetime.datetime.fromtimestamp(statFile.st_atime))

                    # print("размер=", os.path.getsize(file)/1024)
                    # print("изменение=",datetime.datetime.fromtimestamp(os.path.getmtime(file)))
                    # print("создание=",os.path.getctime(file))

                    filewrite.write(pathlib.Path(r+j).suffix+";")
                    filewrite.write(str(statFile.st_size/1024)+";")
                    filewrite.write(str(datetime.datetime.fromtimestamp(statFile.st_mtime))+";")
                    filewrite.write(str(datetime.datetime.fromtimestamp(statFile.st_ctime))+";")
                    filewrite.write(str(datetime.datetime.fromtimestamp(statFile.st_atime))+";")


                    print(node)
                    filewrite.write(str(i)+";")
                    filewrite.write(j+";")

                    for k in node:
                        filewrite.write(k+";")
                    filewrite.write("\n")
                    i += 1
                except FileNotFoundError:
                # except ZeroDivisionError:
                    filewrite.write("FAIL;FAIL;FAIL;FAIL;FAIL;" +str(i)+";")
                    for k in node:
                        filewrite.write(k+";")
                    filewrite.write("\n")
                    i += 1
                    print("\n---FAIL----{{i}}\n")

    filewrite.close()



    #     filewrite()