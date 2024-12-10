# tests/test_login.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.fill.login_form import fill_login_form
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # 
    driver.maximize_window()
    yield driver  
    driver.quit()  

# log in test case | valid
def test_valid_login(driver):
    driver.get("http://localhost:5173/login")  
    
    # clicking the span thingy to set the state to sign in instead of signup ( which is the initial state) 
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/form/div/p[3]/span")
    login_button.click()


    # filling in the login form
    fill_login_form(driver, "crazy@gmail.com", "newpassword1")



    # waiting for my profile text to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='My Profile']"))
    )

    
    try:
        my_profile_text = driver.find_element(By.XPATH, "//p[text()='My Profile']")
        assert my_profile_text.is_displayed(), "'My Profile' text is not displayed"
        print("'My Profile' text is visible.")
    except:
        # checking for the image element that holds the user's pfp (this too indicates that the user has successfully logged in)
        try:
            my_profile_image = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/img[1]')
            assert my_profile_image.is_displayed(), "Profile image wasn't displayed"
        except:
            pytest.fail("Both the checks didn't work.")
