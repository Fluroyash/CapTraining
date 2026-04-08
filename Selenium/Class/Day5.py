from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

"""
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Start']").click()
t=driver.find_element(By.XPATH,"//button[text()='Start']")
driver.implicitly_wait(10)
print(t.text)
"""

"""
driver.get("https://www.decathlon.in")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/shop/Winter-Collection']").click()
driver.implicitly_wait(10)

"""

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[text()='Start']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']")))
ans=driver.find_element(By.XPATH,"//div[@id='finish']")
print(ans.text)