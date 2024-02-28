
import requests
import json
import time 

#习讯云签到脚本
   
data={'account':'21092030121',#账号
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'4.1.5',
      'key':'',
      'model':'SM-G955N',
      'password':'wj030121',#密码
      'platform':'2',
      'registration_id':'160a3797c8437218079',
      'request_source':'3',
      'school_id':'7',#学校代码
      'system':'4.4.2',
      'uuid':'48:45:20:B9:D7:19'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '227',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com/login/api?from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)#登陆成功后返回的信息
token=login_data['data']['token']
time.sleep(1)
#经纬度地址
latitude='33.623806'#维度
longitude='119.018205'#经度
print(login_data)
sign_url='https://api.xixunyun.com/signin?token='+token+'&from=app&version=4.1.5&platform=android&entrance_year=0&graduate_year=0 '
sign_data={'address':'南京市栖霞区八卦洲街道鹂岛路268号八卦洲科创园B栋办公楼1-1039',#签到地址
           'address_name':'南京优宠网络科技有限公司',#签到地点名称
           'change_sign_resource':'0',
           'comment':'',
           'latitude':latitude,
           'longitude':longitude,
           'remark':'0',
    
    }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
print(sign)

