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
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'  # dla emulatora "emulator-5554" (sprawdzic przez adb devices)
        desired_caps['app'] = PATH(
            'C:\APP\ContactManager.apk'  # uwaga nowa aplikacja ContactManager.apk
        )
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_add_contact(self):
        add_button = self.driver.find_element_by_class_name("android.widget.Button")
        add_button.click()
        sleep(2)

        PolaTekstowe = self.driver.find_elements_by_class_name("android.widget.EditText")
        PolaTekstowe[0].send_keys("Marian")
        PolaTekstowe[1].send_keys("4555")
        PolaTekstowe[2].send_keys("aaa@pp.pl")

        el1 = self.assertEqual("Marian", PolaTekstowe[0].text)
        el2 = self.assertEqual("4555", PolaTekstowe[1].text)






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)