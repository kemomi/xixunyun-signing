import requests
import qs 
data = qs.data
signdata = qs.signdata
headers = qs.headers
loginApi = qs.loginApi

# 登录
def login():
  res = requests.post(loginApi, data=data, headers=headers)
  if res and res.json() and res.json().get("data"):
    return res.json().get("data").get("token")
  else:
    return None

# 签到提交
def sign(token):
  signApi = qs.signApi(token)
  res = requests.post(signApi, data=signdata, headers=headers)
  if res and res.json():
    print(res.json().get("code"), res.json().get("message"))
    wechatSend("习讯云签到提交", res.json().get("message"))
    # sendEmail("习讯云签到提交", res.json().get("message"))

# 签到并提交每日体温报告 
token = login()
if token:
  sign(token)
  studentReportInfo(token)

# 日报提交
def studentReportInfo(token):
  studentReportApi = qs.studentReportApi(token)
  studentReportCommitApi = qs.studentReportCommitApi(token)
  res = requests.get(studentReportApi)
  if res.json().get("code") == 20000:
    family_name = res.json().get("data").get("list")[0].get("family_name")
    family_phone = res.json().get("data").get("list")[0].get("family_phone")
    reportForm = qs.reportdata(family_name, family_phone)
    res = requests.post(studentReportCommitApi, data=reportForm)
    print(res.json().get("code"), res.json().get("message"))
    wechatSend("习讯云日报提交", res.json().get("message"))
    # sendEmail("习讯云日报提交", res.json().get("message"))

# 推送微信通知
def wechatSend(type, msg):
  params = {
    "token": qs.token,
    "title": type,
    "content": msg
  }
  res = requests.get("http://www.pushplus.plus/send", params=params)
  print(res)
  if res and res.json() and res.json().get("code") == 200:
    print(type + ",发送微信推送成功")