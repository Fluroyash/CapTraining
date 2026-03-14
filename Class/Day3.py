from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time



a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

"""
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Yash")
driver.quit()

"""

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]').send_keys("rajyashrathore14@gmail.com")
time.sleep(3)
