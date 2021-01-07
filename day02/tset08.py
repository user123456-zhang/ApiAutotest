import pytest
import requests


@pytest.fixture(params=[{"mobilephone": "18043214321", "pwd": "", "rename": "", 'a': "密码不能为空", 'b': "sign_004"},
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
      {"mobilephone": '118012345678', "pwd": 'abc1234', "regname": '', 'a': '手机号码格式不正确', 'b': "sign_016"}])
def register_data(request):
    return request.param


def test_register(register_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.get(url, params=register_data)
    print(f"注册功能，测试数据为：{register_data}")
    print(r.json())
    assert r.json()['msg'] == register_data['a']
