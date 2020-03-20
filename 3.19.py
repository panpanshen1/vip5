#coding:utf-8
# la = 'Lucy|18601914231|男|19890218,Jack|18101913132|女|19810311,Tom|18201912533|女|19830713,Lily|18301911734|男|19870210'
# print(la.find('L'))
import os
# print(os.access('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt',os.F_OK))
# os.chdir('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天')
#print(os.path.isfile('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天') )
import requests,json
import json
# url1='https://api3-core-c-lf.amemv.com/aweme/v1/feed/'
# pa = {''}
# get1= requests.get(url=url1)
# print(get1.json())
# print(json.dumps(get1.content))
# #py变成json
# print(json.loads(get1.content) )
# #json变成pyp
# print(get1.text)
# print(get1.status_code)
# print(get1.headers)
# print(get1.json()) #json结果才可用
# #https://api3-core-c-lf.amemv.com/aweme/v2/feed/?type=0&max_cursor=0&min_cursor=0&count=6&volume=0.07&pull_type=1&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&longitude=116.10007357140303&latitude=37.99688019166357&address_book_access=1&gps_access=1&cached_item_num=0&last_ad_show_interval=1886&mac_address=9C%3A2E%3AA1%3AB9%3AEF%3AD1&preload_aweme_ids&download_sdk_info=%7B%22space_unoccupied%22%3A25889444%7D&action_mask=-1&manifest_version_code=100500&_rticket=1585088788307&app_type=normal&iid=108376696906&channel=local_test&device_type=MI%206&language=zh&uuid=868030039049646&resolution=1080*1920&openudid=8e1174cffbcd65a5&update_version_code=10509900&cdid=462194e0-428b-41f4-9dd3-003c3bef6c59&os_api=28&dpi=480&oaid=2519d807c303a3c7&ac=wifi&device_id=59165485271&mcc_mnc=46000&os_version=9&version_code=100500&effect_channel=local_test&app_name=aweme&version_name=10.5.0&device_brand=Xiaomi&ssmix=a&device_platform=android&aid=1128&ts=1584676175
# print(get1.url)
# #获取url
# print(get1.encoding)
# #获取编码格式
# print(get1.cookies)
# url2 = 'https://auth.pactera.com/login'
# pa = {'service':'http%3A%2F%2Fhub.pactera.com%2F%3Fq%3Dhome-page'}
# get2 = requests.get(url=url2,params=pa)
# print(get2.cookies)
# print(get2.text)
# print(get2.encoding)

# url3 =  'https://auth.pactera.com/login?service=http%3A%2F%2Fhub.pactera.com%2F%3Fq%3Dhome-page'
# da =  {'username':'P0124191','password':'H8%2@#43'}
# header = {'Origin':'https://auth.pactera.com','Cookie':'ga=GA1.2.861240463.1570441658; Hm_lvt_68b002ba3c955428c4e762bbe2945a28=1584519046; Hm_lpvt_68b002ba3c955428c4e762bbe2945a28=1584519046; JSESSIONID=0139EC1FF194DEC2019FCE568393F6C1; SESS3fceb0930b9ea56e5f9be1a327cfb168=6rNzJ7LOwEgRBZu6MKycbdbYt48-h7gULYcp44F8R1E'}
# #da = json.dumps(da)
# #参数处理成json格式
# #post1= requests.post(url=url3,data=da)
# post1=requests.post(url=url3,json=da,headers = header)
# print(post1.encoding)
# print(post1.cookies)
# print(post1.text)
# print(post1.status_code)
# print(post1.headers)
# print(post1.content)

#json对应字典
#json.dumps	将 Python 对象编码成 JSON 字符串---encode编码
#json.loads	将已编码的 JSON 字符串解码为 Python 对象---decode解码




# payload = {'yoyo':True,
#            'json':False,
#            'python':'226296743'}
# py
# print(payload.json(payload))
# print(type(payload))
# #打印类型
# data_json=json.dumps(payload)
# #py转化成json
# data_json1=json.loads(data_json)
# #json转化成py
# print(type(data_json))
# print(data_json)
# print(data_json1)

# url3='https://api2-19-h2-useast2a.musical.ly/aweme/v1/feed/'
# get2=requests.get(url=url3)
#
# data2=json.loads(get2.content)
# #json转化成py
# print(data2['aweme_list'])


# url4 = 'https://lf.snssdk.com/passport/mobile/login/'
# data1 = {'account_sdk_version':'386','_rticket':'1584698846071','iid':'108376696906','uuid':'868030039049646','openudid':'8e1174cffbcd65a5','cdid':'462194e0-428b-41f4-9dd3-003c3bef6c59','oaid':'2519d807c303a3c7'}
# post1  = requests.post(url=url4,data=data1)
# me = post1.json()['message']
# print(me)
# header={}
# header['token']=me
# # s = requests.session()
# # r2 = s.get('https://lf.snssdk.com/passport/mobile/login/')
# # r = json.loads(post1.content)
# # print(r)
# # print((post1.content)[0])
# # print(post1.content)

# url3 = 'https://www.wanandroid.com/user/login'
# data = {'username':'liangchao','password':'123456'}
# r = requests.post(url=url3,data = data)
# cookie = r.cookies
# r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
# print(r2.raw)


# url3 = 'https://www.wanandroid.com/user/login'
# data = {'username':'liangchao','password':'123456'}
# s = requests.session()
# r = requests.post(url=url3,data = data)
# #cookie = r.cookies
# r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
# print(r2.raw)

# url5 = 'https://www.wanandroid.com/user/login'
# data = {'username':'liangchao','password':'123456'}
# r1 = requests.post(url=url5,data = data)
# cookies = {'JSESSIONID':r1.cookies['JSESSIONID']}
# r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookies)
# print(type(r2.text))