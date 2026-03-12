from selenium.webdriver import Edge, EdgeOptions
from time import sleep


a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)



driver.get("https://www.wikipedia.org")
driver.fullscreen_window()
sleep(3)
driver.refresh()
driver.fullscreen_window()
sleep(3)
print("Wikipedia Title:", driver.title)
driver.get("https://www.amazon.in")
driver.fullscreen_window()
sleep(3)
print("Amazon Title:", driver.title)
driver.back()
sleep(3)

driver.back()
sleep(3)
driver.close()