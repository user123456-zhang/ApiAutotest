from base.util import BoxDriver,BasePage,Get_excel
from page.addblock_page import AddBlock
from page.login_page import LoginPage
import unittest
from parameterized import parameterized

class Test_addblock(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html')
        self.page = AddBlock(self.driver)
        self.page.login()

    @parameterized.expand(Get_excel().get(r'ranzhi1\data\data.xlsx','test_info'))
    def test_add(self,block_type,titles):
        try:
            self.page.add_block(block_type,titles)
            realname = self.page.get()
            self.assertEqual(realname,titles,'添加失败')
        except Exception as e:
            print(e)
        finally:
            pass
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()