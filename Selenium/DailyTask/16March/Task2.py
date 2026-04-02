from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://flipkart.in")
sleep(5)
driver.maximize_window()
sleep(5)
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("sunglasses")
sleep(2)
driver.find_element(By.CLASS_NAME,"XFwMiH").click()