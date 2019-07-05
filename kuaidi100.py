import pathlib
import time

import requests
# file_path = r'E:\Onedriver\OneDrive - 广厚设计学校\02_Python\VSCode\Code\Project\myProject\快递查询'
file_path = r''

def init():
    path = pathlib.Path(file_path+'./history.csv')
    # print(path.is_file())

    if path.is_file()==True:
        files = open(file_path+'./history.csv')

        print('**温馨提示**：查询到历史记录，可复制粘贴单号查询：'+'\n',files.read())
        check()
    else:
        print('**温馨提示**：未查询到历史记录，请输入单号查询。\n')
        check()
        
def info(comp_type,num):

    url = 'https://m.kuaidi100.com/query?type={}&postid={}'.format(comp_type,num)
    result = requests.get(url,verify=False)
    for n in range(0,len(result.json()['data'])):
        print(result.json()['data'][n]['time']+'\t',result.json()['data'][n]['context'])
    
    now = time.strftime("%Y.%m.%d\t%H:%M:%S")
    with open(file_path+'./history.csv','a+') as ff:
        ff.write(now+'\t'+comp_type+'\t'+num+'\n')

def check():
    
    num = input('\n请输入快递单号：')
    # num = '1'
    auto_url = 'http://m.kuaidi100.com/autonumber/auto?num={}'.format(num)
    auto_org = requests.get(auto_url)
    if auto_org.json() == []:

        print('\n**温馨提示**：单号有误或未录入，请核对单号或稍后再尝试！\n')
    else:
        comp_type = auto_org.json()[0]['comCode']
        print('=============================')
        print('\n查询结果如下:')
        print('\n快递类型：',comp_type)
        print('快递单号：','\t'+num+'\n')
        info(comp_type,num)

init()


