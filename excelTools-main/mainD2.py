#chsh -s /bin/zsh
#coding:utf-8

from pickletools import uint8
import xlrd
import json

# xlrd版本需要是1.2.0
data = xlrd.open_workbook("/Users/zhaozhihui/Downloads/excelTools-main/Book.xls")
table = data.sheets()[0]
n = table.nrows
stu = []
stu2 = []
json_data = json.dumps(stu,ensure_ascii=False)
with open('/Users/zhaozhihui/Downloads/excelTools-main/numbers.txt','w',encoding='utf-8') as f :
    for i in range(n):
        if i == 0:
            stu2 = table.row_values(i)
            continue
        values = table.row_values(i)
        j = 0
        vs = ""
        val = ""
        v = "【feature_I20220209-0079_20220416_20220312】【JIRA】"
        for value in values:
            a = stu2[j]
            j = j + 1
            if len(str(value)):
                v =  v + "【" + value + "】"
                if a == 'title':
                    val = value
        f.write("{}\n".format(v))
        f.write("{}\n".format(value))
        f.write("{}\n".format("Reviewer:张云波(555012225),杜克瑞(001165980)"))
