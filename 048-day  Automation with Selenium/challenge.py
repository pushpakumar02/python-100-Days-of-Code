from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
e_mail = driver.find_element(By.NAME, "email")

f_name.send_keys("pushpa")
l_name.send_keys("kumar")
e_mail.send_keys("pushpakumar2222000@gmail.com")

sign = driver.find_element(By.CSS_SELECTOR, "form button")
sign.click()
