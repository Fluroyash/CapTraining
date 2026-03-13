from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.get("https://Selenium.dev/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "other languages exist").click()
print(driver.title)
driver.close()