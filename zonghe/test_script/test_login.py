import pytest

from zonghe.baw import Db, Member
from zonghe.caw import DataRead, Asserts


def test_login():
    # 注册用户
    # 下发登录请求
    # 检查结果
    # 删除注册用户
    pass


@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture()
def register(setup_data, url, db, baserequests):
    mobilephone = setup_data['casedata']['mobilephone']
    # 初始化环境
    Db.delete_user(db, mobilephone)
    # 下发注册请求
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 清理环境：删除注册用户（在数据库中添加的数据，测试完成之后清理掉）
    Db.delete_user(db, mobilephone)


@pytest.fixture(params=DataRead.read_yaml(r"data_case/login_data.yaml"))
def login_data(request):
    return request.param


def test_login2(register, login_data, url, baserequests):
    # 下发登录请求
    r = Member.login(url, baserequests, login_data['casedata'])
    # 断言响应结果
    # assert r.json()['msg'] == login_data['expect']['msg']
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['code'] == login_data['expect']['code']
    Asserts.check(r.json(), login_data['expect'], "code,msg,status")


























