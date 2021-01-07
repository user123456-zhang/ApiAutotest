'''
pytest 脚本
1.文件以test_开头
2.测试类以Test开头
3.测试函数或者方法以test_ 开头
一个项目只能有一个pytest.ini配置文件
'''

import requests

url = "http://jy001:8081/futureloan/mvc/api/member/register"


def test_regsiter_001():
    cs = {"mobilephone": "1804", "pwd": "123456"}
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '10001'


def test_regsiter_002():
    cs = {"mobilephone": "18043214321", "pwd": "12345"}
    r = requests.post(url, data=cs)
    assert r.json()['msg'] == '密码长度必须为6~18'


def test_regsiter_003():
    cs = {"mobilephone": "18043214321", "pwd": ""}
    r = requests.post(url, data=cs)
    assert r.json()['msg'] == '密码不能为空'
