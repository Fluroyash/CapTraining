from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

a = Options()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://www.selenium.dev/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Downloads").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Other Languages").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()
time.sleep(2)
print("Page Title:", driver.title)
driver.quit()