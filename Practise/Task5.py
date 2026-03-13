"""
Question 1
"""


from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
a = Options()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, "nav-global-location-popover-link").click()
time.sleep(3)
driver.quit()