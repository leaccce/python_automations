from selenium import webdriver
from selenium.webdriver.common.by import By
import time


website="https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F"

user_id="atulraj.xaviers@gmail.com"
user_password="Atulraj@2853"
id_field='login-username'
password_field='login-password'
login_button='login-button'
driver = webdriver.Edge()
driver.get(website)
driver.implicitly_wait(3)

driver.find_element(By.ID, id_field).send_keys(user_id)
driver.find_element(By.ID, password_field).send_keys(user_password)

driver.find_element(By.ID, login_button).click()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    driver.quit()