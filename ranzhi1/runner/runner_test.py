
from base.HTMLTestRunner import HTMLTestRunner
import unittest 
import time
from base.util import Email
import sys, os
cp = os.path.realpath(__file__)
cd = os.path.dirname(cp)
cd = os.path.dirname(cd)
sys.path.append(cd)
class Test_runnner:

    def runner(self):

        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().discover(r'ranzhi1/test','addblock_test.py'))
        timestamp = time.strftime('%Y-%m-%d_%H_%M_%S')
        report_name = 'report/report_%s.html'%timestamp
        report = open('ranzhi1/%s'%report_name,'wb')
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi自动化测试报告',description='报告详细内容')
        test_runner.run(suite)
        send_address = 'zhangqiang1835198@163.com'
        password = 'NHEXIXBWDXTWBLZR'
        rceivers_address = 'zhang15929849730@163.com'
        title = 'Ranzhi添加区块自动化测试报告'
        annex = 'D:/workspace/selenium/ranzhi1/%s'%report_name
        content = '''
        <p>ranzhi自动化测试报告</p>
        <p>区块添加侧测试完成</p>
        <p>请查收</p>
        <p>谢谢</p>
        '''
        Email().send(send_address,password,rceivers_address,title,annex,content)
if __name__ == "__main__":
    Test_runnner().runner()