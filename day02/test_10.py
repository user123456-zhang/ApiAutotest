"""
mock:
1.一些测试场景难模拟，构造这个场景需要大量的工作
2.测试的功能依赖第三方的接口，但是第三方的接口尚未开发完成
通过mock来模拟接口的返回值。
"""
import requests
import mock

"""
支付接口：
参数：{"订单号"："","支付金额"："","支付方式"：""}
返回值：{"code":200,"msg":"支付成功"}
        {"code":201,"msg":"余额不足"}
        {"code":202,"msg":"支付超时"}
"""


def zhifu(data):
    r = requests.post("http://www.zhifu.com/pay", data=data)
    return r.json


def test_001():
    d = {"订单号": "wx10001", "支付金额": 40.6, "支付方式": "余额宝"}
    # 用mock模拟接口的返回值，return_value是关键字
    zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
    r = zhifu(d)
    print(r)
    assert r['code'] == 200
    assert r['msg'] == "支付成功"


class JinRong:
    def withraw(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/wiehdraw", data=data)
        return r.json()


def test_02():
    d = {"mobilephone": 18012345678, "amount": 10}
    JinRong.withraw = mock.Mock(return_value={'status': 1, 'code': '10001', 'data': None, 'msg': '取现成功'})
    r = JinRong().withraw(d)
    print(r)
    assert r['code'] == '10001'
    assert r['msg'] == '取现成功'
