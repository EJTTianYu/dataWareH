#coding=utf-8

import csv

filename=r'D:\dataWareH\venv\csvPre\account.csv'
with open(filename,'r+') as f:
    data=csv.DictReader(f)
    for row in data:
        max_temp=row['account_id']
        if isinstance(max_temp,int):
            pass
        else:

