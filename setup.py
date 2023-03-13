from setuptools import setup

setup(
  name="qs", # 项目名称
  version="0.1.0", # 项目版本
  description="A script to automate the daily sign-in and report for xixunyun.com", # 项目描述
  py_modules=["qs"], # 项目包含的模块
  install_requires=["requests"], # 项目依赖的第三方库
)