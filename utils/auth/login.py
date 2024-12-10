from selenium.webdriver.common.by import By
from utils.fill.login_form import fill_login_form

def login(driver):
    
    # visit the login page
    driver.get('http:localhost:5173/login')

    # click the login span link | event associated with it 
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/form/div/p[3]/span")
    login_button.click()

    # filling in the login form
    fill_login_form(driver, 'crazy@gmail.com', 'newpassword1')


    