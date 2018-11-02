import json
with open('./case.json','r+') as f:
    data = f.read()
    data = json.loads(data)
    data = json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2)
    f.write(data)
    print(data)
