#coding=utf-8

import csv
<<<<<<< HEAD
import re
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'E:\dataWareH\venv\tablePro\client3.csv'
outF=r'E:\dataWareH\venv\tablePro\client4.csv'

with open(inF,'r') as fin,open(outF,'w',encoding='utf-8') as fout:
=======
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/tablePro/client2.csv'
outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/tablePro/client3.csv'

with open(inF,'r') as fin,open(outF,'w') as fout:
>>>>>>> c13ae3d5b3d8281dfdf9c83a2f4b557477e02827
    #使用csv模块读取文件
    lines=csv.reader(fin)
    #写入文件
    writer=csv.writer(fout,dialect='excel')
<<<<<<< HEAD

    for line in lines:
        try:
            max_temp=line[1]
            #正则匹配出出生月份
            num=re.findall('(\d{2})(\d{2})(\d{2})',max_temp)
            age=int(num[0][0])
            if(0<=age<10):
                line.append('90-100')
            elif(10<=age<20):
                line.append('80-90')
            elif (20 <= age < 30):
                line.append('70-80')
            elif (30 <= age < 40):
                line.append('60-70')
            elif (40 <= age < 50):
                line.append('50-60')
            elif (50 <= age < 60):
                line.append('40-50')
            elif (60 <= age < 70):
                line.append('30-40')
            elif(70<=age<80):
                line.append('20-30')
            elif (80 <= age < 90):
                line.append('10-20')
            elif (90 <= age <= 99):
                line.append('0-10')
            writer.writerow(line)
        except:
            line.append('sex')
            writer.writerow(line)
=======
    #使用一个list排查第一列的相同元素
    for line in lines:
        try:
            max_temp=line[3]
            if(max_temp!='sex'):
                writer.writerow(line)
            else:
                print(','.join(line))

        except:
            print(','.join(line))
>>>>>>> c13ae3d5b3d8281dfdf9c83a2f4b557477e02827
