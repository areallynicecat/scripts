# utils/form_helper.py
from selenium.webdriver.common.by import By

def fill_signup_form(driver, name, email, password):
    """
    Fills the signup form with provided credentials.
    """
    # Find form fields (adjust the CSS selectors as needed for your form)
    name_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')  # Name input field
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')  # Email input field
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')  # First password field

    # Fill out the form fields
    name_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(password)

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()