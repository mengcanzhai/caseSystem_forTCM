headline = ['caesId','id','name','sex','age','preliminary','CC','HOPI','diagnosis','diagnosisTCM','change','prescription','other']
dictionary = {'caesId':'病例编号','id':'患者登记号','name':'姓名','sex':'性别','age':'年龄','preliminary':'初诊复诊','CC':'主诉','HOPI':'现病史','change':'较前变化的症状','prescription':'处方','diagnosis':'西医诊断','diagnosisTCM':'中医诊断','other':'备注'}

def caseobj(caseId):
    case = {}
    for i in range(len(headline)):
        cn = dictionary[headline[i]]
        if i == 0:
            case[cn] = caseId
        elif i in [1,2,3,4,5,6]:
            string = input('{0}:'.format(cn))
            case[cn] = string
            print('{0}:{1}'.format(cn,string))
        elif i == 7:
            TempHOPI = ''
            while True:
                string = input('{0}:'.format(cn))
                if string != 'end':
                    TempHOPI = TempHOPI + string
                else:
                    break
            case[cn] = TempHOPI
            print('{0}:{1}'.format(cn,TempHOPI))
        elif i in [8,9,12]:
            case[cn] = []
            while True:
                string = input('{0}:'.format(cn))
                if string != 'end':
                    case[cn].append(string)
                else:
                    break
            print('{0}:{1}'.format(cn,case[cn]))
        elif i == 10:
            case[cn] = {}
            while True:
                change = input('较前改变的症状:')
                how = input('如何改变:')
                if change != 'end':
                    case[cn][change] = how
                else:
                    break
            print('{0}:{1}'.format(cn,case[cn]))
        elif i == 11:
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
                        if yao == 'end' or quantity == 'end':
                            break
                        else:
                            if quantity[-1] in [1,2,3,4,5,6,7,8,9,0]:
                                quantity = quantity + 'g'
                            fangyao[yao] = quantity
                    fang.append(fangyao)
                    case[cn].append(fang)
            print('{0}:{1}'.format(cn,case[cn]))
    return case
data = caseobj('000000')
print(data)