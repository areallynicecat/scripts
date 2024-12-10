import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.auth.login import login

# initialization
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver  
    driver.quit()  

# booking appointment | valid
def test_get_appointment(driver):

    login(driver)

    # going to the dermatologist component
    driver.get("http://localhost:5173/doctors/Dermatologist")  

    # find and click bilal 
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div[3]/div/p[1]"))
)
    doctor_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div[3]/div/p[1]")
    doctor_element.click()


    # finding and clicking the first available day
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/p[1]"))
    )
    day_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/p[1]")
    # day_text = day_element.text  # getting the text t
    # print(f"Selected Day: {day_text}")  # Print the day text to the console
    day_element.click()

    # finding and selecting the first available time 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[2]/div[2]/p[1]"))
    )
    time_element = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[2]/p[1]")
    # time_text = time_element.text  # Get the time text (e.g., 10
    # print(f"Selected Time: {time_text}")  # Print the time to the console
    time_element.click()

    # clicking book appointment
    book_button = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/button")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(book_button)
    )
    book_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]"))
    )
    
    parent_element = driver.find_element(By.XPATH, "/html/body/div/div/div[1]")
    toastify_element = driver.find_elements(By.CLASS_NAME, "Toastify")

    # if toastify_element:
    #     print('toastify foudn')
    # else:
    #     print('toastify not foudn')


    if len(parent_element.find_elements(By.XPATH, "./*")) > 0 or len(toastify_element) > 0:
        print("The booking was successful!")
    else:
        raise AssertionError("Booking unsuccessful. Child elements not found!")

    # Step 6: Visit the "My Appointments" page
    driver.get("http://localhost:5173/my-appointments")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]"))
    )
