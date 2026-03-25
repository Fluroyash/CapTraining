from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

"""
driver.get("file:///C:/Users/Yash/Desktop/testing.html")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"imp1").send_keys("check")
sleep(2)
driver.switch_to.frame("Name1")
driver.find_element(By.ID,"imp2").send_keys("check 2")
sleep(2)
driver.switch_to.frame("Name2")
driver.find_element(By.ID,"imp3").send_keys("check 3")
"""

"""
driver.get("file:///C:/Users/Yash/Desktop/testing.html")
sleep(2)
driver.find_element(By.ID, "input").send_keys("Wallah")

driver.switch_to.frame('name1')
# driver.switch_to.frame(0)
driver.find_element(By.ID, "input2").send_keys("habi")
driver.switch_to.frame('name2')
# driver.switch_to.frame(0)
driver.find_element(By.ID, "input3").send_keys("biii")
# driver.switch_to.parent_frame()
driver.switch_to.default_content()
sleep(3)

# driver.find_element(By.ID, "input2").send_keys("Wallah Habibii I am Back")
driver.find_element(By.ID, "input").send_keys("  Wallah")
"""

"""
driver.get("https://testautomationpractice.blogspot.com/#")
sleep(2)
driver.maximize_window()
#---------------------I---------Simple ALert---------------
# driver.find_element(By.ID, 'alertBtn').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
#-------------------II-------Confirmation Alert-------------------
driver.find_element(By.ID, 'confirmBtn').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
# alert.dismiss()
sleep(5)
driver.quit()
"""

"""
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '(//a[. = "Python 3.14.3"])[4]').click()
"""

driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
