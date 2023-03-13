你需要创建一个qs.py的文件，用来存放你的数据和函数，比如你的登录信息，签到信息，报告信息，以及一些生成API地址或表单数据的函数。你可以参考以下示例，但是你需要根据你自己的实际情况修改其中的内容和参数：

# 你的登录信息
data = {
  "username": "your_username",
  "password": "your_password"
}

# 你的签到信息
signdata = {
  "temperature": "36.5",
  "healthState": "1",
  "dangerousRegion": "2",
  "dangerousRegionRemark": "",
  "contactSituation": "2",
  "contactSituationRemark": "",
  "familySituation": "1",
  "familySituationRemark": ""
}
# 你的请求头
headers = {
  "Content-Type": "application/json;charset=UTF-8"
}

# 你的登录API地址
loginApi = "https://api.xixunyun.com/login/api"

# 根据token生成签到API地址的函数
def signApi(token):
  return f"https://api.xixunyun.com/signin/student?token={token}"

# 根据token生成日报API地址的函数
def studentReportApi(token):
  return f"https://api.xixunyun.com/studentReport/info?token={token}"

# 根据token生成日报提交API地址的函数
def studentReportCommitApi(token):
  return f"https://api.xixunyun.com/studentReport/commit?token={token}"

# 根据家庭姓名和电话生成报告表单数据的函数
def reportdata(family_name, family_phone):
  return {
    "family_name": family_name,
    "family_phone": family_phone,
    "temperature": "36.5",
    "health_state": "1",
    "dangerous_region": "2",
    "dangerous_region_remark": "",
    "contact_situation": "2",
    "contact_situation_remark": "",
    "family_situation": "1",
    "family_situation_remark": ""
  }

# 你的微信推送token
token = "your_token"