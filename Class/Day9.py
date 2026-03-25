from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.get("https://www.amazon.in")
