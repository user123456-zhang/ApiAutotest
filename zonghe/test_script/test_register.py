"""
注册的测试脚本
"""
import pytest

from zonghe.baw import Member, Db

from zonghe.caw import DataRead, BaseRequests, Asserts


# 注册失败的测试脚本
@pytest.fixture(params=DataRead.read_yaml(f"data_case/register_fail.yaml"))
def fail_data(request):
    return request.param


def test_register_fail(url, baserequests, fail_data):
    # 下发注册请求
    print(f"{fail_data}")
    r = Member.register(url, baserequests, fail_data['data'])
    # 断言响应的结果

    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # assert r.json()['status'] == fail_data['expect']['status']
    Asserts.check(r.json(), fail_data['expect'], "code,msg,status")


# 把注册成功的数据写到register_pass.yaml
# 注册成功的脚步，下发请求，断言响应的结果


@pytest.fixture(params=DataRead.read_yaml(f"data_case/register_pass.yaml"))
def pass_data(request):
    return request.param


def test_register_pass(url, baserequests, pass_data, db):
    mobilephone = pass_data['data']['mobilephone']
    # 初始化环境
    Db.delete_user(db, mobilephone)
    # 下发注册请求
    r = Member.register(url, baserequests, pass_data['data'])
    print(r.text)
    # 断言响应结果
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    # assert r.json()['status'] == pass_data['expect']['status']
    Asserts.check(r.json(),pass_data['expect'], "code,msg,status")
    # 调用查询的接口，在查询的结果中能找到本次注册的手机号
    r1 = Member.list(url, baserequests)
    assert mobilephone in r1.text
    # 清理环境：删除注册用户（在数据库中添加的数据，测试完成之后清理掉）
    Db.delete_user(db, mobilephone)


@pytest.fixture(params=DataRead.read_yaml(r"data_case/register_repeat.yaml"))
def repeat_data(request):
    return request.param


def test_register_repeat(url, baserequests, repeat_data, db):
    mobilephone = repeat_data['data']['mobilephone']
    # 初始化环境
    Db.delete_user(db, mobilephone)
    # 下发注册请求
    Member.register(url, baserequests, repeat_data['data'])
    # 重复注册
    r = Member.register(url, baserequests, repeat_data['data'])
    print(r.text)
    # 断言响应的结果
    # assert r.json()['code'] == register_data['expect']['code']
    # assert r.json()['msg'] == register_data['expect']['msg']
    # assert r.json()['status'] == register_data['expect']['status']
    Asserts.check(r.json(), repeat_data['expect'], "code,msg,status")
    # 清理环境：删除注册用户（在数据库中添加的数据，测试完成之后清理掉）
    Db.delete_user(db, mobilephone)
