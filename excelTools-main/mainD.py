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
        f.write("{}\n".format("IMWealthEentTracking *entTrackModel = [[IMWealthEentTracking alloc] init];"))
        for value in values:
            a = stu2[j]
            j = j + 1
            if len(str(value)):
                b = str(a)
                c = b.upper()
                v = ''
                if c == 'OP_ID':
                    v = "entTrackModel." + c + ' = ' +'[IMFiveMaiDianTool getOPID:curpagename lastStr:'+ '@"' + str(value) +'"];'
                elif c == 'CURPAGENO':
                    v = "entTrackModel." + c + ' = ' + '[IMFiveMaiDianTool getCurpageno:curpagename];'
                else:
                    v = "entTrackModel." + c + ' = @"' +str(value)+'";'
                f.write("{}\n".format(v))
        f.write("{}\n".format("[[IMICBCWealthService sharedIMICBCWealthService] uploadBehaviorAnalysis:entTrackModel];"))
        f.write("{}\n".format("------"))

with open('stu_json.json','r') as f:
    d = json.load(f)
    print(d)
    r = list(filter(lambda j: j[2] > 5, d))
    print("亲密度大于5的人有:",r)
