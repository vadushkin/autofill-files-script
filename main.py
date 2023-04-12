import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

# Absolute path to pdf files
ABSOLUTE_PATH_TO_PDFS = os.getenv("ABSOLUTE_PATH_TO_PDFS")
os.chdir(ABSOLUTE_PATH_TO_PDFS)

# ['1.pdf', '2.pdf', ... 'n.pdf']
file_paths = os.listdir()

# Login
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()

driver.get('https://www.mymusicsheet.com/library')
time.sleep(5)

xpath_btn_login = '/html/body/root-cmp/div/div/library/div[2]/mp-blank/div[3]/mp-button/button'
driver.find_element(By.XPATH, xpath_btn_login).click()

# For animation
time.sleep(1)

xpath_email = '/html/body/modal-container/div[2]/div/login-modal/div/div[2]/km-login/form/mp-input[1]/div/label/input'
xpath_password = '/html/body/modal-container/div[2]/div/login-modal/div/div[2]/km-login/form/mp-input[2]/div/label/input'

email_btn = driver.find_element(By.XPATH, xpath_email)
password_btn = driver.find_element(By.XPATH, xpath_password)

# Login
email_btn.send_keys(EMAIL)
password_btn.send_keys(PASSWORD)

xpath_btn_login2 = '/html/body/modal-container/div[2]/div/login-modal/div/div[2]/km-login/form/mp-button[1]/button'

button = driver.find_element(By.XPATH, xpath_btn_login2)
button.click()

# Second animation
time.sleep(5)

for index, file_path in enumerate(file_paths, start=1):
    # Base outcome
    if file_path[-4:] != '.pdf':
        continue

    # Generate a path to a pdf file
    if ABSOLUTE_PATH_TO_PDFS[-1] == '/':
        abs_path_to_pdf = ABSOLUTE_PATH_TO_PDFS + file_path
    else:
        abs_path_to_pdf = ABSOLUTE_PATH_TO_PDFS + '/' + file_path

    xpath_pdf_upload_file = '/html/body/root-cmp/div/div/library/div[2]/div/library-files/div[2]/mp-callout/div[' \
                            '2]/library-file-selector/div/input'
    driver.find_element(By.XPATH, xpath_pdf_upload_file).send_keys(abs_path_to_pdf)

    # For download, you can choose a different value for your convenience
    time.sleep(10)

    print(f"Iteration №{index}")

driver.close()
driver.quit()
