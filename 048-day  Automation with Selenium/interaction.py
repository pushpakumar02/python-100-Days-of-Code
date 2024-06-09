from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#creating a driver
driver = webdriver.Chrome(options=chrome_options)
# navigating to wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# article = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
# print(articles_count)

# Find element by Link Text
all_portal = driver.find_element(By.LINK_TEXT, "Content portals")
all_portal.click()

# find the "search" <input> by NAME
search = driver.find_element(By.NAME, "search")
# sending key word input to selenium
search.send_keys("python", Keys.ENTER)