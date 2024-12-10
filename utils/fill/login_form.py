# utils/form_helper.py
from selenium.webdriver.common.by import By

def fill_login_form(driver, email, password):
    """
    Fills the signin form with provided credentials.
    """
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')  # Email input field
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')  # First password field

    # Fill out the form fields
    email_field.send_keys(email)
    password_field.send_keys(password)


    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()