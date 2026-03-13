from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
a = Options()
a.add_experimental_option("detach", True)
driver = Edge(options=a)


driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("123456")
time.sleep(3)
driver.quit()