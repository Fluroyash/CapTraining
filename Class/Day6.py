from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
"""
driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(15)
links=driver.find_elements(By.TAG_NAME,'a')
print(links)
print(len(links))
for i in links:
    print(i.text)

driver.quit()
"""
"""
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys("watches")
driver.find_element(By.ID,'nav-search-submit-button').click()

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
driver.quit()
"""

"""
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(15)
ele=driver.find_element(By.XPATH,'//a[@class="gb_A"]')
print(ele.get_attribute('aria-label'))

"""

"""
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(15)
ele=driver.find_element(By.XPATH,'//a[contains(@class,"nav-a")and text()="Mobiles"]')
print(ele.get_attribute('href'))
"""

"""
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(15)
ele=driver.find_element(By.XPATH,'//input[@type="text"]')
print(ele.is_displayed())
print(ele.is_enabled())
"""


"""
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
driver.implicitly_wait(15)
ele=driver.find_element(By.XPATH,'//button[text()="Register now"]')
print(ele.is_displayed())
print(ele.is_enabled())
driver.quit()

"""
"""
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(15)
btn1 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]')
print(btn1.is_selected())
btn2 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[2]')
print(btn2.is_selected())
driver.quit()
"""
"""
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID,"firstName").send_keys("Yash")
driver.find_element(By.ID,"lastName").send_keys("Rathore")
driver.find_element(By.ID,"userEmail").send_keys("yash@gmail.com")
driver.find_element(By.CLASS_NAME,"form-check.form-check-inline").click()
driver.find_element(By.ID,"userNumber").send_keys("90244***")
driver.find_element(By.ID,"dateOfBirthInput").send_keys("")
driver.find_element(By.ID,"dateOfBirthInput").send_keys("14 Nov 2004")
driver.find_element(By.ID,"subjectsInput").send_keys("Math")
driver.find_element(By.CLASS_NAME,"form-check-label").click()
driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
driver.quit()
"""


driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID, "firstName").send_keys("Yash")
driver.find_element(By.ID, "lastName").send_keys("Rathore")
driver.find_element(By.ID, "userEmail").send_keys("yash@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("9876543210")
dob = driver.find_element(By.ID, "dateOfBirthInput")
dob.send_keys(Keys.CONTROL + "a")
dob.send_keys("14 Nov 2004")
dob.send_keys(Keys.ENTER)
driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur, Rajasthan")
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.ID, "submit").click()
driver.quit()

