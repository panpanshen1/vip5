import requests,json
#导入包




#get请求
# urlstr='https://zhuanlan.zhihu.com/p/62234258'
# #调用get方法
# result = requests.get(url=urlstr)
#
# #打印结果
# print(result.text)
# print(result.cookies)
# print(result.headers)
# print(result.encoding)
# url1 = 'https://wiki.bytedance.net/pages/viewpage.action'
# payload1 = {'pageId':'52897307'}
# result1=requests.get(url=url1,params=payload1)
# print(result1.content)
#
# url2 = 'https://wiki.bytedance.net/pages/viewpage.action'
# payload2 = {'pageId':'211142976','preview':'/211142976/211142993/jubao.json'}
# result2=requests.get(url=url2,params=payload2)
# print(result2.status_code)

# url3='https://www.taobao.com/'
# result3=requests.get(url=url3)
# print(type(result3))





# #post请求
# #help(requests),这个包的使用
# url4 = 'http://httpbin.org/post'
# data1={'qq群名':'selenium+jemeter+loadrunner','qq群号':'106014970'}
# data1=json.dumps(data1)
# result4=requests.post(url=url4,data=data1)
# print(type(result4))
# print(result4.json())
# print(result4.text)
#
#
# url5 = 'http://httpbin.org/post'
# data2={'qq群名':'selenium+jemeter+loadrunner','qq群号':'106014970'}
# #data2=json.dumps(data1)
# result5=requests.post(url=url5,json=data2)
# print(result4.json())
# print(result4.text)
#
#



# url6='https://www.wanandroid.com/user/login'
# header1 = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
# data3 = {'username':'chaoge','password':'123456'}
# result6=requests.post(url=url6,data=data3,headers=header1)
# print(result6.text)
# print(result6.headers)






# url7='https://www.wanandroid.com/user/login'
# data7 = {'username':'chaoge','password':'123456'}
# se = requests.Session()
# #初始化session对象
#
# result7 = requests.post(url=url7,data=data7)
#result8 = se.get('https://www.wanandroid.com/lg/'/ntodo/list/0)
#上面的'/n需要去掉等测试的时候
# result9 = se.get('https://www.wanandroid.com/tools/decimal')
# print('******',result8.text)
# print('******',result7.text)
# print('******',result9.text)






