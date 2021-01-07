from base.util import BasePage,BoxDriver
from time import sleep





class LoginPage(BasePage):

    def login(self):
        driver = self.driver

        #用户名
        driver.input('id account','admin')

        #密码
        driver.input('id password','123456')

        #登录
        driver.click('id submit')

        #点击项目
        driver.click('x //*[@id="s-menu-3"]')
        #进入iframe-3
        driver.switch_to_frame('id iframe-3')
        sleep(2)
if __name__ == "__main__":
    LoginPage(BoxDriver).login()