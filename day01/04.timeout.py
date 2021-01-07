'''
timeout 超时
1.上传文件：上传2M时比较耗时，但是2G的文件，耗时更久，可以使用超时timeout设置比较长的超时时间
2.接口测试时，测试接口的性能，返回结果是否在某个时间范围内。
    比如获取用户列表的接口，是否在10ms以内。
'''


import requests

url = "http://jy001:8081/futureloan/mvc/api/member/list"
# read time out
r = requests.get(url, timeout=0.1) # 100ms
print(r.text)

'''
代理 proxies
1.用界面操作某个功能，结果正常，但是用自动化操作同意的功能，报错。
    界面操作是，抓包
    自动化脚本执行时，抓包
    对比抓到的包，检查差异点
2.频繁的想服务器发起请求，服务器当做共计处理，将ip地址禁掉了。使用代理IP发送请求
'''

url = "http://jy001:8081/futureloan/mvc/api/member/list"
proxy = {
    "http": "http://127.0.0.1:8888", # HTTP协议，使用http://127.0.0.1:8888 代理
    "https": "http://127.0.0.1:8888"
}
r = requests.get(url, proxies=proxy) # 设置代理后，要把相应的代理工具fiddler打开
print(r.text)
# https的请求，使用代理是，需要设置忽略证书
r = requests.get("https://www.baidu.com", proxies=proxy, verify=False)
print(r.text)















