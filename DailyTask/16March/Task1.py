from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time

a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://amazon.com")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
sleep(3)
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(3)
price = driver.find_element(By.XPATH,"//span[text()='Samsung Galaxy S26 Ultra, Unlocked Android Smartphone + $200 Gift Card, 512GB, Privacy Display, Galaxy AI, AI Camera, Super Fast Charging 3.0, Durable Battery, 2026, US 1 Year Warranty, Black']/../../../..//span[@class='a-price-whole']")
sleep(3)
print(price.text)
driver.find_element(By.XPATH,"//span[text()='Samsung Galaxy S26 Ultra, Unlocked Android Smartphone + $200 Gift Card, 512GB, Privacy Display, Galaxy AI, AI Camera, Super Fast Charging 3.0, Durable Battery, 2026, US 1 Year Warranty, Black']").click()
sleep(3)
driver.quit()