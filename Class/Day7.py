from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)

"""
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
curr = driver.find_element(By.ID, 'currentAddress')
curr.send_keys("Jaipur, Rajasthan")
curr.send_keys(Keys.CONTROL,'a')
curr.send_keys(Keys.CONTROL,'c')
sleep(2)
perm = driver.find_element(By.ID, 'permanentAddress')
perm.send_keys(Keys.CONTROL,'v')
driver.quit()
"""

"""
driver.get('https://demoqa.com/buttons')
driver.maximize_window()
sleep(2)
# driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()
# sleep(2)
single_click = driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]")
action = ActionChains(driver)
action.click(single_click).perform()
double_click = driver.find_element(By.ID,'doubleClickBtn')
action.double_click(double_click).perform()
sleep(2)
right_click = driver.find_element(By.ID,'rightClickBtn')
action.context_click(right_click).perform()
sleep(3)
action.scroll_by_amount(0,500).perform()
sleep(5)

driver.quit()
"""

"""
action = ActionChains(driver)
driver.get('https://amazon.in/')
driver.maximize_window()
sleep(2)
ele=driver.find_element(By.ID,"nav-link-accountList")
sleep(2)
action.move_to_element(ele).perform()
sleep(5)
driver.quit()
"""

driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()


"""
task 1
mouse hover test.automation.com
copy text
drag and drop 

task 2 
using action chains hover the mouse on kids 
after that click on it 
then a scroll
and then click on the shop and then scroll and click on any shoe 
after that select one size and click on add to bag

task 3
open flipkart perform scroll action 
click on myntra from new tab switch back to the tab 
after that fetch all the window id title and url 


 
"""