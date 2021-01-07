import requests
from time import sleep

url = "http://jy001:8081/futureloan/mvc/api/member/register"
url_1 = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = [{"mobilephone": "18043214321", "pwd": "", "rename": "", 'a': "密码不能为空", 'b': "sign_004"},
      {"mobilephone": "", "pwd": "123456", "rename": "", 'a': "手机号不能为空", 'b': "sign_005"},
      {"mobilephone": "", "pwd": "", "rename": "", 'a': "手机号不能为空", 'b': "sign_006"},
      {"mobilephone": "18043214322", "pwd": "", "rename": "丫丫", "a": "密码不能为空", 'b': "sign_007"},
      {"mobilephone": '', "pwd": 'aaa58585', "regname": 'wawa', 'a': "手机号不能为空", 'b': "sign_008"},
      {"mobilephone": '18043214322', "pwd": 'aaa58', "regname": '', 'a': '密码长度必须为6~18', 'b': "sign_009"},
      {"mobilephone": '18043214322', "pwd": 'aaa', "regname": '', 'a': '密码长度必须为6~18', 'b': "sign_010"},
      {"mobilephone": '18043214322', "pwd": 'aaaaaa1952154126415', "regname": '', 'a': '密码长度必须为6~18', 'b': "sign_011"},
      {"mobilephone": '1', "pwd": 'abc1234', "regname": '', 'a': '手机号码格式不正确', 'b': "sign_011"},
      {"mobilephone": '180432', "pwd": 'abc1234', "regname": '', 'a': '手机号码格式不正确', 'b': "sign_012"},
      {"mobilephone": '1804321432', "pwd": 'abc1234', "regname": '', 'a': '手机号码格式不正确', 'b': "sign_013"},
      {"mobilephone": '118043214321', "pwd": 'abc1234', "regname": '', 'a': '手机号码格式不正确', 'b': "sign_014"},
      {"mobilephone": '11111111111', "pwd": 'abc1234', "regname": '', 'a': '手机号码格式不正确', 'b': "sign_015"},
      {"mobilephone": '118012345678', "pwd": 'abc1234', "regname": '', 'a': '手机号码已被注册', 'b': "sign_016"},
      {"mobilephone": "18043214322", "pwd": "123456", "rename": "", 'a': '注册成功', 'b': "sign_001"},
      {"mobilephone": "18043214322", "pwd": "123456", "rename": "haha", 'a': '注册成功', 'b': "sign_002"}
      ]
cs_1 = [{"mobilephone": "18043214321", "pwd": "", 'a': "密码不能为空", 'b': "sign_003"},
        {"mobilephone": "", "pwd": "123456", 'a': "手机号不能为空", 'b': "sign_004"},
        {"mobilephone": "", "pwd": "", 'a': "手机号不能为空", 'b': "sign_005"},
        {"mobilephone": "18043214333", "pwd": "", 'a': "手机号未注册", 'b': "sign_006"},
        {"mobilephone": "180", "pwd": "123456", "a": "密码不能为空", 'b': "sign_007"},
        {"mobilephone": '1804321421', "pwd": '12345', 'a': "密码长度必须为6~18", 'b': "sign_008"},
        {"mobilephone": '18043214322', "pwd": 'aaa58222', 'a': '密码错误', 'b': "sign_009"},
        {"mobilephone": '18043214321', "pwd": '123456', 'a': '登录成功', 'b': "sign_001"},
        ]
for i in range(len(cs)):
    r = requests.get(url, params=cs[i])
    assert r.json()['msg'] == cs[i]["a"]
    print('测试用例' + cs[i]['b'] + ':测试成功')
    sleep(2)

for i in range(len(cs_1)):
    r = requests.get(url_1, params=cs_1[i])
    assert r.json()['msg'] == cs_1[i]["a"]
    sleep(2)
    print('测试用例' + cs_1[i]['b'] + ':测试成功')