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
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung").click()
time.sleep(3)
driver.quit()