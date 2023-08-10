from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://python.org")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget div ul li time")
for date in dates:
    print(date.text)
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget div ul li a')

for event in events:
    print(event.text)

upcoming_events = {n : {'time': dates[n].text, 'name': events[n].text} for n in range(len(dates))}
print(upcoming_events)

driver.quit()



