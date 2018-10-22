#coding=utf-8

import csv
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/card.csv'
outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/card1.csv'

with open(inF,'r') as fin,open(outF,'w') as fout:
    #使用csv模块读取文件
    lines=csv.reader(fin)
    #写入文件
    writer=csv.writer(fout,dialect='excel')
    #判断是否存在非三个字段的脏数据
    for line in lines:

        if(line[2]=='classic' or line[2]=='junior' or line[2]=='gold'):
            writer.writerow(line)
        else:
            print(','.join(line))
