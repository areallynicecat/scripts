# tests/test_signup.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.fill.signup_form import fill_signup_form
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.get_credentials import get_credentials, edit_credentials

# initializing the test
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver  
    driver.quit()

# sign Up test case | valid
def test_valid_signup(driver):
    driver.get("http://localhost:5173/login")  
    
    credentials = get_credentials()
    print(credentials)
    name, email, password = credentials
    edit_credentials()

    # filling in the sign up form
    fill_signup_form(driver, name, email, password)

    

    # waiting for the paraprah with my profile to load in | shouldn't really need this as it's running locally
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='My Profile']"))
    )

    
    try:
        my_profile_text = driver.find_element(By.XPATH, "//p[text()='My Profile']")
        assert my_profile_text.is_displayed(), "The 'My Profile' wasn't found "
    except:
        # searching for the profile image img element if my profile is not visible 
        try:
            my_profile_image = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/img[1]')
            assert my_profile_image.is_displayed(), "Profile image ain't displayed"
        except:
            pytest.fail("Both the checks didn't work.")

