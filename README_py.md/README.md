# qs

qs是一个Python脚本，可以帮助你自动完成xixunyun.com网站上的每日签到和报告。

## 功能

- 自动登录xixunyun，获取token和用户信息。
- 自动签到，提交温度和健康状况。
- 自动填写日报，提交家庭姓名、电话、温度和健康状况。
- 自动推送签到和报告结果到微信。

## 用法

1. 安装requests模块：

```bash
python -m pip install requests

修改qs.py文件中的data、signdata、reportdata和token变量，填入你自己的登录信息、签到信息、报告信息和微信推送token。

## 运行

python main.py

## 输出
查看输出结果或者微信推送消息，确认签到和报告是否成功。

在你的项目文件夹中，创建一个名为`main.py`的文件，用来调用qs模块中的函数，实现签到和报告的逻辑。你可以参考以下示例，但是你需要根据你自己的项目修改其中的内容和参数：

```python
import qs # 导入qs模块
import requests # 导入requests模块

# 登录xixunyun.com网站，获取token和用户信息
response = requests.post(qs.loginApi, json=qs.data, headers=qs.headers)
token = response.json()["data"]["token"]
user = response.json()["data"]["user"]

# 签到，提交温度和健康状况
response = requests.post(qs.signApi(token), json=qs.signdata, headers=qs.headers)
sign_result = response.json()["message"]

# 填写日报，提交家庭姓名、电话、温度和健康状况
response = requests.get(qs.studentReportApi(token), headers=qs.headers)
report_id = response.json()["data"]["id"]
response = requests.post(qs.studentReportCommitApi(token), json=qs.reportdata(user["family_name"], user["family_phone"]), headers=qs.headers)
report_result = response.json()["message"]

# 推送签到和报告结果到微信
message = f"【签到结果】{sign_result}\n【报告结果】{report_result}"
requests.get(f"https://sc.ftqq.com/{qs.token}.send?text={message}")
```

## 打包
```python
python setup.py sdist bdist_wheel
```

这个命令会在你的项目文件夹中生成一个名为dist的子文件夹，里面包含了打包好的项目文件。