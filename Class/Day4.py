
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

"""
driver.get("https://demoqa.com")
driver.maximize_window()
sleep(3)
driver.get('http://demoqa.com/webtables')
salary = driver.find_element(By.XPATH,"//td[text() = 'Cierra']/..//td[5]")
print('Salary of Cierra', salary.text)  
"""

"""
driver.get("https://the-internet.herokuapp.com/tables")
driver.maximize_window()
sleep(3)
due=driver.find_element(By.XPATH,"//td[text()='Frank']/..//td[4]")
print(due.text)
"""
