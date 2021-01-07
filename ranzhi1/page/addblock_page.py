
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random
from base.util import BoxDriver
from page.login_page import LoginPage

class AddBlock(LoginPage):


    def add_block(self,block_type,titles):
        #点击添加区块
        driver = self.driver
        driver.click('x //*[@id="dashboard"]/div[2]')
        sleep(1)
        #点击框
        driver.select_by_index('id blocks','%s'%('1' if block_type=='任务列表' else '2'))

        if block_type == '任务列表':
            driver.input('id title',titles)

            #选择宽度
            driver.select_by_index('id grid','%s'%random.randint(1,5))


            #选择颜色
            driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
            sleep(1)
            driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%s]'%(random.randint(1,6)))
            sleep(1)

            #选择类型
            driver.click('x //*[@id="paramstype_chosen"]')
            sleep(1)
            driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%s]'%(random.randint(1,5)))
            
            #数量
            driver.clear('id params[num]')
            driver.input('id params[num]','%s'%(random.randint(1,15)))
            sleep(1)
            #排序
            driver.click('x //*[@id="paramsorderBy_chosen"]')
            driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%s]'%(random.randint(1,6)))

            #任务状态
            driver.click('x //*[@id="paramsstatus_chosen"]/ul')
            driver.click('x //*[@id="paramsstatus_chosen"]/div/ul/li[%s]'%(random.randint(1,6)))

            #b保存
            driver.click('id submit')
            sleep(3)

        else :
            #区块名称
            driver.input('id title',titles)

            #选择宽度
            driver.select_by_index('id grid','%s'%(random.randint(1,5)))


            #选择颜色
            driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
            sleep(1)
            driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%s]'%(random.randint(1,6)))
            sleep(2)

            #状态
            driver.click('id paramsstatus_chosen')
            sleep(1)
            driver.click('x //*[@id="paramsstatus_chosen"]/div/ul/li[%s]'%(random.randint(1,4)))

            #数量
            driver.clear('id params[num]')
            driver.input('id params[num]','%s'%random.randint(1,15))
            sleep(1)

            #排序
            driver.click('x //*[@id="paramsorderBy_chosen"]')
            driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%s]'%(random.randint(1,6)))

            #b保存
            driver.click('id submit')
            sleep(3)

    def get(self):
        accounts = self.driver.find_elements('xpath /html/body/div/div/div[1]/div/div[1]/div[1]')
        account = accounts[-1] 
        return account.text.split('\n')[1].strip()

if __name__ == "__main__":
    pass


        # assert account.text.split('\n')[1].strip() == titles
        # sleep(2)
        # driver.click('x //*[@id="dashboard"]/div[2]')
        # sleep(2)

