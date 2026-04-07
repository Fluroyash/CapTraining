from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.parametrize('uname,password',[('standard_user','secret_sauce'),('locked_out_user','secret_sauce'),('problem_user','secret_sauce'),('performance_glitch_user','secret_sauce'),('error_user','secret_sauce'),('visual_user','secret_sauce')])
def test_1(uname,password):
    a = EdgeOptions()
    a.add_experimental_option("detach", True)
    driver = Edge(options=a)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"user-name").send_keys(uname)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url,"Login Failed"
    driver.quit()