from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#print(article_count.text)
#article_count.click()

article_count = driver.find_element(By.LINK_TEXT, '6,682,162')
#article_count.click()

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.RETURN)



#driver.quit()