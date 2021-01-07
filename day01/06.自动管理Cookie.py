'''
自动管理Cookie
request 中的Session类，能够自动获取和管理Cookie。
'''

import requests

# 新建一个Session
s = requests.session()
print(s.cookies)
# 登录接口 login
# 使用session发送请求
loginData = {
    "account": "2780487875@qq.com",
    "password": "qq2780487875"
}
r = s.post("https://www.bagevent.com/user/login", data=loginData)
# print(r.text)

# dashboard 接口
r = s.post("https://www.bagevent.com/user/dashboard")
# print(r.text)
print(s.cookies)

# 退出登录 logout
r = s.post("https://www.bagevent.com/user/logout")
# print(r.text)
print(s.cookies)

# RequestsCookieJar 转成字典
d = requests.utils.dict_from_cookiejar(s.cookies)
print(d)