from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.get("https://twitter.com/")
driver.maximize_window()
sleep(5)
frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(frame)
driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()
sleep(5)
driver.quit()







