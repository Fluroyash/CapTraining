from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[@role='button']").click()
driver.find_element(By.NAME,"q").send_keys("Lipstick")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
wait = WebDriverWait(driver,10)
name = wait.until(EC.visibility_of_element_located((By.XPATH,"(//a[@title='MARS Ultra Pigmented Creamy Matte Lipstick'])[1]")))
print(name.text)
driver.close()