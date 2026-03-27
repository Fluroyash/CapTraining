import os.path
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
driver.get("https://www.amazon.in")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH, "(//div[@class='nav-div'])[6]").click()
expected = 'https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers'
actual = driver.current_url

assert expected == actual, "You are on wrong page"
driver.quit()
"""

"""
driver.get("https://www.google.com")
driver.maximize_window()
sleep(5)
driver.save_screenshot("google.png")
folder = os.path.join(os.getcwd(), "files")
os.makedirs(folder, exist_ok=True)
sleep(5)
driver.save_screenshot(f'{folder}/google.png')
sleep(2)
#driver.quit()

ele = driver.find_element(By.XPATH, "//textarea[@title='Search']")
#ele.screenshot(f"{folder}/screenshot_ele.png")
#   timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
"""

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.find_element(By.ID,'user-name').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('user')
driver.find_element(By.ID,'login-button').click()
expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url
if expected == actual:
    pass
else:
    driver.save_screenshot('screenshot2.png')

sleep(5)

driver.quit()
