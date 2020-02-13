import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.POM_Unit_Tests.Pages.HomePage import HomePage

class TestRecommendation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\CS4DS & SWT++\Recommend Me\lib\chromedriver.exe")

    def testRecommendation(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        home = HomePage(driver)
        home.enterMovieName("Avatar")
        time.sleep(1)
        home.clickSearch()
        time.sleep(1)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

# with adding the below piece of code you are able to run without unit case command
if __name__ == '__main__':
    unittest.main()
# TearDown, run after every test / TearDownClass, will run only once, run at the end of all the tests.
