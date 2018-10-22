#coding=utf-8

import csv
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/tablePro/card1.csv'
outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/tablePro/card2.csv'

ref=r'/Users/tianyu/PycharmProjects/dataWareH/venv/tablePro/disp2.csv'
with open(ref,'r') as refe:
    rows=csv.reader(refe)
    list1=[]
    for row in rows:
        try:
            dist=row[0]
            if dist not in list1:
                list1.append(dist)
        except:
            print('error')
print(list1)

with open(inF,'r') as fin,open(outF,'w') as fout:
    #使用csv模块读取文件
    lines=csv.reader(fin)
    #写入文件
    writer=csv.writer(fout,dialect='excel')
    count=0
    for line in lines:
        try:
            max_temp=line[1]
            if (max_temp in list1):
                writer.writerow(line)
            else:
                count=count+1
        except:
            print(','.join(line))
print(count)