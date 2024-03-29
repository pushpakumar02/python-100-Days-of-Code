# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# ACCOUNT_NUMBER = "...."
# ACCOUNT_PASSWORD = '....'
#
#
# #  Keep the browser open (helps diagnose issues if the script crashes)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://tinder.com/app/recs")
#
# sleep(2)
# accept = driver.find_element(By.XPATH, value='//*[@id="t425926696"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
# accept.click()
#
# sleep(2)
# login_button = driver.find_element(By.XPATH, value='//*[@id="t425926696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
# login_button.click()
#
# sleep(2)
# more_option = driver.find_element(By.XPATH, value='//*[@id="t-1302454380"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
# more_option.click()
#
#
# sleep(2)
# fb_login = driver.find_element(By.XPATH, value='//*[@id="t-1302454380"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div/div')
# fb_login.click()
#
# # #Switch to Facebook login window
# # sleep(2)
# # base_window = driver.window_handles[0]
# # fb_login_window = driver.window_handles[1]
# # driver.switch_to.window(fb_login_window)
# # print(driver.title)
#
# # Login and hit enter
# sleep(2)
# email = driver.find_element(by=By.NAME, value='email')
# email.send_keys(ACCOUNT_NUMBER)
# password = driver.find_element(by=By.NAME, value='pass')
# password.send_keys(ACCOUNT_PASSWORD)
# password.send_keys(Keys.ENTER)
#
# #Switch back to Tinder window
# driver.switch_to.window(base_window)
# print(driver.title)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = '.....'
FB_PASSWORD = '.....'

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
