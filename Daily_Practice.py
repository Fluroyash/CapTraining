'''
Question 1

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
'''



'''
Question 2
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
import time

a = Options()
a.add_experimental_option("detach", True)

driver = Edge(options=a)

driver.get("https://www.wikipedia.org")

print("Current URL is:", driver.current_url)

time.sleep(3)
driver.quit()
'''



'''
Question 3

from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
import time
a = Options()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.get("https://www.wikipedia.org")
time.sleep(2)
driver.refresh()
time.sleep(2)
print("Wikipedia Title:", driver.title)
driver.get("https://www.amazon.in")
time.sleep(2)
print("Amazon Title:", driver.title)
driver.back()
time.sleep(2)
driver.close()
'''