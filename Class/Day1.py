
'''
from selenium.webdriver import Edge, EdgeOptions
from time import sleep


a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.get("https://demoqa.com")
driver.fullscreen_window()

title=driver.title
print(title)
print(driver.current_url)

name = driver.name
print(name)
sleep(7)
#driver.close()
driver.quit()

'''

from selenium.webdriver import Edge, EdgeOptions
from time import sleep


a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

driver.get("https://amazon.in/")
driver.maximize_window()

driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()