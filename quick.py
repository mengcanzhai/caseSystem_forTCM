import json
from collections import OrderedDict
headline = ['caesId','id','date','name','sex','age','preliminary','CC','HOPI','diagnosis','diagnosisTCM','change','prescription','other']
dictionary = {'caesId':'病例编号','id':'患者登记号','name':'姓名','sex':'性别','age':'年龄','preliminary':'初诊复诊','CC':'主诉','HOPI':'现病史','change':'较前变化的症状','prescription':'处方','diagnosis':'西医诊断','diagnosisTCM':'中医诊断','other':'备注','date':'日期'}

def caseobj(caseId):
    case = OrderedDict()
    for i in range(len(headline)):
        cn = dictionary[headline[i]]
        if i == 0:
            case[cn] = caseId
        elif i in [1,2,3,4,5,6,7]:
            string = input('{0}:'.format(cn))
            case[cn] = string
            print('{0}:{1}'.format(cn,string))
        elif i == 8:
            TempHOPI = ''
            while True:
                string = input('{0}:'.format(cn))
                if string != 'end':
                    TempHOPI = TempHOPI + string
                else:
                    break
            case[cn] = TempHOPI
            print('{0}:{1}'.format(cn,TempHOPI))
        elif i in [9,10,13]:
            case[cn] = []
            while True:
                string = input('{0}:'.format(cn))
                if string != 'end':
                    case[cn].append(string)
                else:
                    break
            print('{0}:{1}'.format(cn,case[cn]))
        elif i == 11:
            case[cn] = {}
            while True:
                change = input('较前改变的症状:')
                how = input('如何改变:')
                if change != 'end':
                    case[cn][change] = how
                else:
                    break
            print('{0}:{1}'.format(cn,case[cn]))
        elif i == 12:
            case[cn] = []
            while True:
                jishu = input('剂数:')
                jixing = input('剂型:')
                fangfa = input('服用方法:')
                if jishu == 'end' or jixing == 'end' or fangfa == 'end':
                    break
                else:
                    fang = [jishu,jixing,fangfa]
                    fangyao = {}
                    while True:
                        yao = input('药名:')
                        quantity = input('剂量:')
                        if yao == 'end' or quantity == 'end' or yao == '' or quantity == '':
                            break
                        else:
                            if quantity[-1] in ['1','2','3','4','5','6','7','8','9','0']:
                                quantity = quantity + 'g'
                            fangyao[yao] = quantity
                    fang.append(fangyao)
                    case[cn].append(fang)
            print('{0}:{1}'.format(cn,case[cn]))
    return case


def checkId(path):
    with open(path,'r') as f:
        data = f.read()
        if data == '':
            outputId = input('输入初始序号:')
            outputId = '{0:0>6}'.format(outputId)
            return outputId,[]
        else:
            data = json.loads(data)
            i = int(data[-1]['病例编号'])
            i = i+1
            outputId = '{0:0>6}'.format(i)
            return outputId,data

def main():
    path = './case.json'
    caseId,originalData = checkId(path)
    newcase = []
    while True:
        cmd = input('是否新建病例{0}?y/n'.format(caseId))
        if cmd == 'y':
            newcase.append(caseobj(caseId))
            caseId = '{0:0>6}'.format(int(caseId)+1)
        else:
            print('退出编辑')
            break
    newcase = originalData + newcase
    data = json.dumps(newcase,ensure_ascii=False,sort_keys=True,indent=2)
    with open(path,'w') as f:
        f.write(data)
        print('保存成功')


main()

