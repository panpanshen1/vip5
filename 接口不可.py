import requests,json
'''
re = requests.get(url='https://www.baidu.com')
print(re.status_code,'\n',re.headers,end='\n')
'''
'''
payload = {
    'k':'Java'
}
re = requests.get(url='https://wanandroid.com/wxarticle/list/405/1/json',params = payload)
print(type(re.content))
print(type(re.json()))
dict1 = re.json()
print(dict1)
print(dict1['data']['curPage'])
'''
#post方法，参数为表单
'''
payload ={
    'username':'liangchao',
    'password':'123456'
}
url='https://wanandroid.com/user/login'
re = requests.post(url=url,data = payload)
print(re.text)
'''
'''
payload ={
    'username':'liangchao',
    'password':'123456'
}
payload1=json.dumps(payload)#dict->json
print(type(payload1))
#json.loads()#json->dict
url='https://wanandroid.com/user/login'
re = requests.post(url=url,data = payload1)
print(re.text)
'''


'''
payload1 ={
    'username':'liangchao',
    'password':'123456'
}
payload2 ={
    'name':'liangchao',
    'link':'123456'
}
url1='https://wanandroid.com/user/login'
url2 ='https://wanandroid.com/lg/collect/addtool/json'
s = requests.session()
re = s.post(url=url1,data = payload1)
re2=s.post(url = url2,data = payload2)
print(re2.text,re2.status_code)
'''

'''
payload2 ={
    'username':'liangchao',
    'password':'123456'
}
url2 ='http://httpbin.org/post'
#s = requests.session()

re2=requests.post(url = url2,data = payload2)
print(re2.text,re2.status_code)
'''

