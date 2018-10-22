#coding=utf-8

import csv
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/loan1.csv'
outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/loan2.csv'

with open(inF,'r') as fin,open(outF,'w') as fout:
    #使用csv模块读取文件
    lines=csv.reader(fin)
    #写入文件
    writer=csv.writer(fout,dialect='excel')
    count=0
    for line in lines:
        try:
            max_temp=int(line[4])
            dur=int(line[7])
            if (max_temp>=dur):
                #list1.append(max_temp)
                writer.writerow(line)
            else:
                count=count+1
        except:
            print(','.join(line))
print(count)
