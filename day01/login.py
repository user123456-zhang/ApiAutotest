import requests

# 1.验证用户使用合法的手机号、密码，昵称为空，注册成功
url = "http://jy001:8081/futureloan/mvc/api/member/register"
# cs = {"mobilephone": "18043214321", "pwd": "123456", "rename": ""}
# r = requests.get(url, params=cs)
# print(r.text)
# assert r.json()["msg"] == "注册成功"
#
# # 2.验证用户使用合法的手机号、密码、昵称，注册成功
# cs = {"mobilephone": "18043214322", "pwd": "123456", "rename": "haha"}
# r = requests.get(url, params=cs)
# assert r.json()['msg'] == '注册成功'

# 4.验证用户使用合法的手机号码，昵称、密码为空，注册失败
cs = {"mobilephone": "18043214322", "pwd": "", "rename": ""}
r = requests.get(url, params=cs)

assert r.json()['msg'] == '密码不能为空'

# 5.验证用户手机号码、昵称为空，密码合法，注册失败
cs = {"mobilephone": "", "pwd": "123456", "rename": ""}
r = requests.get(url, params=cs)
assert r.json()['msg'] == '手机号不能为空'

# 6.验证用户手机号码、密码、昵称为空，注册失败
cs = {"mobilephone": "", "pwd": "", "rename": ""}
r = requests.get(url, params=cs)
assert r.json()['msg'] == '手机号不能为空'

# 7.验证用户使用合法的手机号码、昵称，密码为空，注册失败
cs = {"mobilephone": "18043214322", "pwd": "", "rename": "丫丫"}
r = requests.get(url, params=cs)
assert r.json()['msg'] == '密码不能为空'

# 8.验证用户手机号码为空，密码、昵称合法，注册失败
cs = {"mobilephone": '', "pwd": 'aaa58585', "regname": 'wawa'}
r = requests.get(url, params=cs)
print(r.text)
assert r.json()['msg'] == '手机号不能为空'

# 9.验证用户使用合法的手机号码，密码输入5位，注册失败
cs = {"mobilephone": '18043214322', "pwd": 'aaa58', "regname": ''}
r = requests.get(url, params=cs)
print(r.text)
assert r.json()['msg'] == '密码长度必须为6~18'

# 10.验证用户使用合法的手机号码，密码输入3位，注册失败
cs = {"mobilephone": '18043214322', "pwd": 'aaa', "regname": ''}
r = requests.get(url, params=cs)
print(r.text)
assert r.json()['msg'] == '密码长度必须为6~18'

# 11.验证用户使用合法的手机号码，密码输入19位，注册失败
cs = {"mobilephone": '18043214322', "pwd": 'aaaaaa1952154126415', "regname": ''}
r = requests.get(url, params=cs)
print(r.text)
assert r.json()['msg'] == '密码长度必须为6~18'