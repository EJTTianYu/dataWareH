#coding=utf-8

import csv
import re
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/client.csv'
outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/client1.csv'

with open(inF,'r') as fin,open(outF,'w') as fout:
    #使用csv模块读取文件
    lines=csv.reader(fin)
    #写入文件
    writer=csv.writer(fout,dialect='excel')

    for line in lines:
        try:
            max_temp=line[1]
            #正则匹配出出生月份
            num=re.findall('(\d{2})(\d{2})(\d{2})',max_temp)
            if (int(num[0][1])>50):

                line.append('female')
                writer.writerow(line)
            else:
                line.append('male')
                writer.writerow(line)

        except:
            line.append('sex')
            writer.writerow(line)
