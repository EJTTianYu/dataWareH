#coding=utf-8

import csv
#建立输入输出两个文件流，一个用于读取原csv文件的数据，一个用于存储处理之后的csv文件数据
inF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/trans2.csv'
outF=r'/Users/tianyu/PycharmProjects/dataWareH/venv/csvAft/trans3.csv'

with open(inF,'r') as fin,open(outF,'w') as fout:
    #使用csv模块读取文件
    lines=csv.reader(fin)
    #写入文件
    writer=csv.writer(fout,dialect='excel')
    count=17526
    c1=count*0.65
    c2=count*0.17
    c3=count*0.105
    c4=count*0.075
    for line in lines:
        try:
            symbol=line[7]
            if (symbol==' ' and c1>0):
                line[7]='SIPO'
                writer.writerow(line)
                c1=c1-1
            elif(symbol==' ' and c2>0):
                line[7]='DUCHOD'
                writer.writerow(line)
                c2=c2-1
            elif(symbol==' ' and c3>0):
                line[7] = 'POJISTNE'
                writer.writerow(line)
                c3=c3-1
            elif(symbol==' ' and c4>0):
                line[7] = 'UVER'
                writer.writerow(line)
                c4=c4-1
            else:
                writer.writerow(line)

        except:
            print(','.join(line))


