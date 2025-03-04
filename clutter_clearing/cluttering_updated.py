import os
import shutil
import argparse
def a():
    os.makedirs('PDFs',exist_ok=True)
    os.makedirs('Images',exist_ok=True)
    os.makedirs('Texts',exist_ok=True)

    text_list=[i for i in os.listdir() if ".txt" in i]
    image_list=[i for i in os.listdir() if ".png" in i]
    pdf_list=[i for i in os.listdir() if ".pdf" in i]

    [shutil.move(j,f"Texts") for j in text_list]
    [shutil.move(j,f"Images") for j in image_list]
    [shutil.move(j,f"PDFs") for j in pdf_list]
    
import os
import shutil

def clearing(file_type):
    os.makedirs(file_type, exist_ok=True)
    files = os.listdir()
    holder = [i for i in files if file_type in i]
    for j in holder:
        shutil.move(j, file_type)


def c(path,filetype):
    if path is None:
        path="r"
        a()
        if filetype is None:
            filetype="r"
        else:
            clearing(filetype)
    else:
        os.chdir(path)
        a()
        if filetype is None:
            filetype="r"
        else:
            clearing(filetype)

p=argparse.ArgumentParser()
p.add_argument("-o","--path",help="enter the directory you want to clear ",default=None)
p.add_argument("-f","--filetype",type=str,help="enter the file type you want to clear ",default=None)
args=p.parse_args()

c(args.path,args.filetype)