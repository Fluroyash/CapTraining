from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
import time

a = Options()
a.add_experimental_option("detach", True)

driver = Edge(options=a)

driver.get("https://www.wikipedia.org")

print("Page Title is:", driver.title)

time.sleep(3)
driver.quit()