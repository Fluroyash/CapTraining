from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By


a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[@href='http://www.facebook.com/nopCommerce']").click()
sleep(5)
driver.switch_to.window(driver.window_handles[1])
sleep(5)
driver.find_element(By.XPATH,"//input[@aria-label='Email or phone']").send_keys("Abs@gmailk.com")
sleep(2)
driver.find_element(By.XPATH,"//input[@aria-label='Password']").send_keys("saumya123")
sleep(2)
driver.find_element(By.XPATH,"//div[@aria-label='Log in']").click()