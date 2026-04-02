from time import sleep

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Yashl")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Raj Singh Rathore")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("yash14@gmail.com")
driver.find_element(By.XPATH, "//input[@id='age']").send_keys("21")
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("100000")
driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Q&T")
driver.find_element(By.XPATH, "//button[@id = 'submit']").click()

salary = driver.find_element(By.XPATH, "//td[text() = 'Yash']/..//td[5]")
print("The Salary is:",salary.text)

driver.quit()