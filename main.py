class caseInput:
    #病例编号、患者登记号、姓名、性别、年龄、初诊、主诉、现病史（包括症状、四诊）、症状改变、方药
    headline = ['caesId','id','name','sex','age','preliminary','CC','HOPI','change','prescription']
    dictionary = {'caesId':'病例编号','id':'患者登记号','name':‘'姓名','sex':'性别','age':'年龄','preliminary':'初诊/复诊','CC':'主诉','HOPI':'现病史','change':'较前变化的症状','prescription':'处方'}
    def __init__(self,caseId):
        self.stack = 1
        self.caseId = caseId
        self.isCmd = 0
        self.case = {'caseId':caseId}
        
    def cmdMonitor(self,string):
        string = input('{0}：'.format(dictionary[headline[self.stack]]))
        if string[0] == '.':
            if string[1:] == l

    def simpleInput(self,headline):


    def id(self):
        id = input('病例号：')
        case['id'] = id
        if len(stack) == 1:
            stack[0] =1
        else:

