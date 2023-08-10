from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

