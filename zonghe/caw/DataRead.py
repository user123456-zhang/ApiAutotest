"""
读文件相关的方法
"""
import configparser
import os

import yaml


def get_project_path():
    """
    获取当前工程路径
    :return:
    """
    cp = os.path.realpath(__file__)  # D:\ApiAutoTest\zonghe\caw\DataRead.py
    # print(cp)
    cd = os.path.dirname(cp)  # D:\ApiAutoTest\zonghe\caw
    # print(cd)
    return os.path.dirname(cd) + "\\"  # D:\ApiAutoTest\zonghe\


def read_ini(file_path, key):
    """
    读取ini配置文件
    :param file_path: 配置文件的路径
    :param key: key值
    :return: key对应的value
    """
    file_path = get_project_path() + file_path
    config = configparser.ConfigParser()
    config.read(file_path)
    return config.get("env", key)  # env对应ini文件中的[env]


def read_yaml(file_path):
    """
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    """
    file_path = get_project_path() + file_path
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return yaml.load(content, Loader=yaml.FullLoader)


# 测试代码，用完删除
# if __name__ == '__main__':
#     print(read_yaml(r"data_case/register_fail.yaml"))
#     url = read_ini(r"data_env\env.ini", "url")
#     print(url)
#     db = read_ini(r"data_env\env.ini", "db")
#     print(db)
#     db = eval(db)  # 字符串解析为字典
#     print(db)
#     print(type(db))
#     get_project_path()
