from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import yaml
import openpyxl
from selenium.webdriver.support import expected_conditions as EC
import logging,sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
'''工具类'''


class BoxDriver:

    def __init__(self,browser_type='Chrome',url=None):
        # 根据传入的参数，创建响应的浏览器对象
        if browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser_type == 'Opera':
            self.driver = webdriver.Opera()
        elif browser_type == 'Safari':
            self.driver = webdriver.Safari()
        elif browser_type == 'Ie':
            self.driver = webdriver.Ie()
        else:
            raise NameError('浏览器类型%s没找到！'%browser_type)

        self.get(url)
        # 最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def get(self,url):
        '''
        打开指定的网页
        url: 网页地址
        '''
        self.driver.get(url)

    def maximize_window(self):
        '''
        窗口最大化
        '''
        self.driver.maximize_window()

    def minimize_window(self):
        '''
        窗口最小化
        '''
        self.driver.minimize_window()

    def implicitly_wait(self,second=10):
        '''
        隐式等待
        second:等待的最大时间，单位是秒
        '''
        self.driver.implicitly_wait(second)

    def convert_selector_to_locator(self,selector,separator=' '):
        '''
        定位方式解析器，将形如：
        'id account' 
        的自定义方式，解析为selenium标准定位方式：
        By.ID,'account'
        selector: 自定义定位方式
        sepatrator: 分隔方式，默认使用' '来分隔
        '''
        # 定位方式
        by = selector.split(separator)[0].strip()
        # 定位方式对应的值
        value = selector.split(separator)[1].strip()


        if by == 'id' or by == 'i':
            locator = (By.ID,value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME,value)
        elif by == 'class_name' or by == 'c':
            locator = (By.CLASS_NAME,value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME,value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT,value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT,value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH,value)
        elif by == 'css_selector' or by == 'cs':
            locator = (By.CSS_SELECTOR,value)
        else:
            raise NameError('请输入一个合法的定位方式！')
        
        return locator

    def find_element(self,selector):
        '''
        定位单个元素
        selector:自定义定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        return self.driver.find_element(*locator)

    def find_elements(self,selector):
        '''
        定位多个元素
        selector: 自定义定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        return self.driver.find_elements(*locator)
    
    def input(self,selector,text):
        '''
        向元素输入文本
        selector：自定义定位方式
        text：要输入的文本
        '''
        element = self.find_element(selector)
        element.clear() #写文本之前，先清空一下
        element.send_keys(text)

    def click(self,selector):
        '''
        单击元素
        selector：自定义定位方式
        '''
        self.find_element(selector).click()

    def switch_to_frame(self,selector):
        iframe = self.find_element(selector)
        self.driver.switch_to_frame(iframe)

    def select_by_index(self,selector,index):
        '''
        根据index选择下拉框内容
        selector：自定义选择器
        index：下标
        '''
        select = self.find_element(selector)
        options = Select(select)
        options.select_by_index(index)
    def select_by_value(self,selector,value):

        '''
        根据value选择下拉框内容
        selector：自定义选择器
        value：属性
        '''
        select = self.find_element(selector)
        options = Select(select)
        options.select_by_value(value)


    def select_by_visible_text(self,selector,visible_text):
        '''
        根据visible_text选择下拉选择框的内容
        selector: 自定义选择器
        visible_text: 可见文本
        '''
        select = self.find_element(selector)
        options = Select(select)
        options.select_by_visible_text(visible_text)

    def close(self):
        '''
        关闭当前浏览器窗口
        '''
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()

    def switch_to_parent(self):
        '''
        退回到父框架
        '''
        self.driver.switch_to.parent_frame()

    def clear(self,selector):
        '''
        清空输入框
        '''
        element = self.find_element(selector)
        element.clear()


    def wait(self,second):
        '''
        休眠
        second:休眠时间
        '''
        
        time.sleep(second)
    def webdriver_wait(self,second1='10',second2='0.5',selector=None):
        '''
        显示等待
        second1=超时时间(秒) ，默认等待10秒
        second2=采样间隔(秒),默认刷新频率0.5秒 
        '''
        locator = self.convert_selector_to_locator(selector)
        a = WebDriverWait(self.driver,second1,second2).until(EC.presence_of_element_located(locator))
        return a
class BasePage:

    def __init__(self,driver:BoxDriver):
        self.driver = driver
        
class GetYaml:

    '''
    读取yamml格式文件，返回一个 字典类型的数据
    path:yaml文件的路径
    '''

    def get(self,path):
        with open(path,'r',encoding='utf-8') as file:
            config = yaml.load(file.read(),Loader=yaml.FullLoader)
            return config

class Get_excel:

    def get(self,path,worksheet):
        '''
        打开工作表薄,读取Excel格式文件，返回一个列表类型的数据
        path：excel文件路径
        worksheet：工作表的名称
        '''
        workbook = openpyxl.load_workbook(path)
        login_success = workbook[worksheet]
        a = []
        for row in login_success:
            e = []
            for cell in row:
                e.append(cell.value)
            a.append(tuple(e))
        return a[1:]


class GetCSV:

    def get(self,path):
        '''
        读取CSV文件
        '''
        with open(path,'r',encoding='utf-8') as file:
            lines = file.readlines()
            return [tuple(e.strip() for e in line.split(',')) for line in lines][1:]

class GetLogger:

    def __init__(self,path):
        '''
        path:设置文件路径
        '''
        self.path = path
        #创建日志
        self.logger = logging.getLogger()
        #设置日志级别
        self.logger.setLevel(logging.DEBUG)
        #设置日志输出的格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:%(message)s')

    def console(self,level,message):
        '''

        '''
        '''写入到控制台'''
        fh = logging.FileHandler(self.path,encoding='utf-8')
        #设置文件级别
        fh.setLevel(logging.DEBUG)
        #设置日志格式
        fh.setFormatter(self.formatter)
        #将内容添加到日志中
        self.logger.addHandler(fh)

        '''写到控制台'''
        #创建一个流处理器
        sh = logging.StreamHandler(sys.stdout)
        #设置日志等级
        sh.setLevel(logging.DEBUG)
        #设置日志格式
        sh.setFormatter(self.formatter)
        #将流处理器添加到日志中
        self.logger.addHandler(sh)
        
        
        #判断日志等级，进行相应的输出
        if level =='debug':
            self.logger.debug(message)
        elif level =='info':
            self.logger.info(message)
        elif level =='waring':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        fh.close()
        
    def info(self,message):
        self.console('info',message)

    def debug(self,message):
        self.console('debug',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)

    def critical(self,message):
        self.console('critical',message)
        

class Email:

    def send(self,send_address,password,rceivers_address,title,annex,content,server='smtp.163.com',port= 25):
        '''
        server:邮件服务器地址
        port:服务器端口
        send_address：发件人地址
        password:密码(或授权码)
        receivers_address:收件人地址
        title:主题
        annex:添加附件(附件路径)
        text:正文
        '''
        #设置邮件服务器地址
        smtpserver = server
        #设置邮件服务器端口
        port = port

        #发件人地址
        sender = send_address

        #密码(授权码：NHEXIXBWDXTWBLZR)
        password = password

        #收件人地址
        receivers = rceivers_address

        #创建邮件对象
        mail = MIMEMultipart()

        #初始化发件人
        mail['from'] = sender
        #添加收件人
        mail['to'] = receivers
        #添加主题
        mail['subject'] = title

        #读取报告内容
        path = annex
        with open(path,'rb') as file:
            report = file.read()
    
        #对附件进行编码
        attachment = MIMEText(report,'base64','utf-8')
        #设置附件的类型
        attachment['Content-Type'] = 'application/octet_stream'
        #设置附件的处理方式
        attachment['Content-Disposition'] = 'attchment;filename=%s'%path.split('/')[-1]
        #添加附件
        mail.attach(attachment)

        #生成邮件正文
        body = MIMEText(content,'html','utf-8')
        #添加正文
        mail.attach(body)

        #创建SMTP对象
        smtp = smtplib.SMTP()
        #连接服务器
        smtp.connect(smtpserver,port)

        smtp.login(sender,password)

        smtp.sendmail(sender,receivers.split(';'),mail.as_string())

        smtp.close()
        print('邮件发送完毕')

if __name__ == "__main__":
    GetLogger('ranzhi.log').info('测试代码！')