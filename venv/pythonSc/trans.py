#coding=utf-8

import csv
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'E:\dataWareH\venv\csvPre\trans.csv'
#outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/trans3.csv'

with open(inF,'r') as fin:
    #使用csv模块读取文件
    lines=csv.reader(fin)
    count=0
    list=[]
    for line in lines:
        try:
            bank=line[8]
            op=line[4]
            if(bank==''):
                count+=1
                if op not in list:
                    list.append(op)
                print(','.join(line))


        except:
            print(','.join(line))
print(list)
print(count)


