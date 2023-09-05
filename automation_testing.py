from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# We can apply POM but here we know that the attributes like ID, XPATH etc will not change that's why implementing unit testing only...

class Selenium_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://localhost:5000/")
        cls.driver.maximize_window()
        time.sleep(5)

    def test_readme_button(self):
        driver=self.driver
        readme=driver.find_element(By.ID,"readme_button")
        driver.execute_script("arguments[0].click()", readme)
        time.sleep(4)

    def test_sentence1_positive(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        input_element = driver.find_element(By.XPATH, "//*[@id='user_input']")
        input_element.send_keys("What do you know about Zaid Ahmed? He must be in the Employee's list" + Keys.ENTER)
        time.sleep(3)

    def test_sentence2_positive(self):
        driver=self.driver
        driver.find_element(By.XPATH,"//*[@id='user_input']").send_keys("tell me something about Quaid-e-Azam? Is he present in our Owners list?" + Keys.ENTER)
        time.sleep(3)

    def test_sentence3_negative(self):
        driver=self.driver
        driver.find_element(By.XPATH,"//*[@id='user_input']").send_keys("Can you give me the phone number of Lara Khan?" + Keys.ENTER)  #
        time.sleep(3)

    # due to teardown class there's an error coming because the application is already running on the local host (main.py)

if __name__ == "__main__":
    unittest.main()
    unittest

