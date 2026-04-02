'''
Locaters
'''

'''
DEMOQA
from selenium.webdriver import Edge, EdgeOptions
import time
from selenium.webdriver.common.by import By

a = EdgeOptions()
a.add_experimental_option("detach", True)

driver = Edge(options=a)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.ID, "userName").send_keys("Fluro")

time.sleep(3)


driver.find_element(By.ID, "userEmail").send_keys("kuchbhi@gmail.com")
time.sleep(3)
driver.find_element(By.ID, "currentAddress").send_keys("yahan")
time.sleep(3)
driver.find_element(By.ID, "permanentAddress").send_keys("wahan")
time.sleep(3)
driver.find_element(By.ID, "submit").click()
time.sleep(3)
driver.close()

'''


'''
Amazon Task
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)

driver = Edge(options=a)

driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(5)

class testin:
    def jus(self):
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("shirts")
        driver.find_element(By.ID, "nav-search-submit-text").click()


        time.sleep(3)

obj = testin()
obj.jus()

'''
"""

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)

driver = Edge(options=a)

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CLASS_NAME,'nav-input.nav-progressive-attribute').send_keys("shirts")
time.sleep(3)
driver.find_element(By.ID, "nav-search-submit-text").click()
time.sleep(3)
driver.close()

"""


"""
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)

driver = Edge(options=a)
driver.get('https://demoqa.com/text-box')
driver.maximize_window()
time.sleep(3)
search = driver.find_element(By.TAG_NAME, 'input')
searchButton = driver.find_element(By.TAG_NAME, 'textarea')
search.send_keys('Yash')
searchButton.send_keys('Jaipur')
time.sleep(3)
driver.close()
"""
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

"""
driver.get('https://www.amazon.in/')
time.sleep(3)
searchButton = driver.find_element(By.LINK_TEXT, 'Customer Service')
searchButton.click()
time.sleep(3)
driver.close()
"""



driver.get("https://Selenium.dev/")

driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Downloads").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "other languages exist").click()

print(driver.title)

driver.quit()



