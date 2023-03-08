from gensim import models
from tqdm import tqdm
import numpy as np
import chardet
import os

root = "address"
list = os.listdir(root)
dataset_train = []
dataset_test = []

for cat in list:
    if cat in '0' or cat in '1':
        print(cat)
        files = os.listdir(root + cat)
        for i,f in enumerate(files):
            fname = root + cat + "/" + f
            
            #파일 열어서 인코딩 확인
            rawdata = open(fname, 'rb').read()
            result = chardet.detect(rawdata)
            enc = result['encoding']

            #인코딩 맞게 열기
            file = open(fname, "r", encoding = enc)
            strings = file.read()
            
            if i<450:
                if(cat=='1'):
                    dataset_train.append(['__label__보이스피싱',strings])
                else:
                    dataset_train.append(['__label__일반',strings])
            else:
                if(cat=='1'):
                    dataset_test.append(['__label__보이스피싱',strings])
                else:
                    dataset_test.append(['__label__일반',strings])
            file.close()


with open("address"+".txt",'w',encoding='utf-8') as file:
    for i in range(len(dataset_train)):
        file.write(dataset_train[i][0]+"\t"+dataset_train[i][1]+"\n")

print(len(dataset_train),len(dataset_test))
