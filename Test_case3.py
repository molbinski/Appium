import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('C:\APP\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_testing_wifii_options_api_demos(self):
        property_tab = self.driver.find_element_by_xpath('//*[@text="Preference"]')
        property_tab.click()
        sleep(2)
        preferences_dependencies = self.driver.find_element_by_xpath("//android.widget.TextView[@text='3. Preference dependencies']")
        preferences_dependencies.click()
        sleep(2)
        wifii_checkbox = self.driver.find_element_by_class_name('android.widget.CheckBox')
        wifii_checkbox.click()
        sleep(2)
        wifi_settings = self.driver.find_element_by_xpath("//*[@text='WiFi settings']")
        wifi_settings.click()
        sleep(2)
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('1234')
        sleep(2)
        ok_button = self.driver.find_element_by_xpath("//*[@text='OK']")
        ok_button.click()
        self.driver.keyevent(4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)