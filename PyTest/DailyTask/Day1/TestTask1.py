from time import sleep
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
a = EdgeOptions()
a.add_experimental_option("detach", True)
driver = Edge(options=a)
driver.implicitly_wait(10)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"ico-register").click()
sleep(2)
def test_dt1():
    driver.find_element(By.ID,"gender-male").click()
    sleep(2)
def test_dt2():
    driver.find_element(By.ID,"FirstName").send_keys("Yash")
    sleep(2)
def test_dt3():
    driver.find_element(By.ID,"LastName").send_keys("Rathore")
    sleep(2)
def test_dt4():
    driver.find_element(By.ID,"Email").send_keys("yash@gmail.com")
    sleep(2)
def test_dt5():
    driver.find_element(By.ID,"Password").send_keys("test@123")
    sleep(2)
def test_dt6():
    driver.find_element(By.ID,"ConfirmPassword").send_keys("test@123")
    sleep(2)
def test_dt7():
    driver.find_element(By.ID,"register-button").click()
    sleep(5)
