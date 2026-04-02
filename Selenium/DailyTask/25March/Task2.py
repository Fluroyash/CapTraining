from selenium.webdriver import Edge, EdgeOptions
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.implicitly_wait(10)
import os
driver.get("https://in.pinterest.com/")
driver.maximize_window()
folder=os.path.join(os.getcwd(),'Pinterest')
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/Pinterest_Page.png')