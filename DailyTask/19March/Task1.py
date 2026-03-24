from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys('watch')
driver.find_element(By.ID,"nav-search-submit-button").click()
im1=driver.find_elements(By.XPATH,"//img[@class='s-image']")
print(len(im1))
im1[5].click()
driver.quit()