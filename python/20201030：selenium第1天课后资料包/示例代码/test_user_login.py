import unittest
from selenium import webdriver
from time import sleep


class UserLoginTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://39.106.69.242/thinksns/")
	
	def tearDown(self):
		self.driver.quit()
	
	# 使用正确的账号和正确密码登录成功，进入个人主页
	def test_01_login_success(self):
		email, password = "zhangwuji@qq.com", "333333"
		expected_url = "http://39.106.69.242/thinksns/index.php?s=/Home/index"
		sleep(2)
		self.driver.find_element_by_name("email").send_keys(email)
		sleep(2)
		self.driver.find_element_by_name("passwd").send_keys(password)
		sleep(2)
		self.driver.find_element_by_id("button").click()
		sleep(2)
		self.assertEqual(expected_url, self.driver.current_url)
		sleep(2)
	
	# 使用正确的账号和错误的密码登录失败，进入登录页面
	def test_02_login_fail_with_wrong_password(self):
		email, password = "zhangwuji@qq.com", "333334"
		expected_url = "http://39.106.69.242/thinksns/index.php?s=/Index/login/t/1"
		sleep(2)
		self.driver.find_element_by_name("email").send_keys(email)
		sleep(2)
		self.driver.find_element_by_name("passwd").send_keys(password)
		sleep(2)
		self.driver.find_element_by_id("button").click()
		sleep(2)
		self.assertEqual(expected_url, self.driver.current_url)
		sleep(2)
	

if __name__ == '__main__':
	unittest.main(verbosity=2)