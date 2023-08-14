from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, "fName")
name.send_keys("Jaloliddin")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Sultonov")
email = driver.find_element(By.NAME, "email")
email.send_keys("sultonovjaloliddin07@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()

input("hello")


