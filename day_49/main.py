from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.linkedin.com/home?original_referer=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F')
    page.get_by_role("button", name="Accept").click()

    page.get_by_label("Email or phone").fill("alistairedwardjenkins@gmail.com")
    page.get_by_label("Password").filter(has_not_text="Show").fill("AlexJackGeo3")

    page.get_by_role("button").filter(has_text="Sign in").click()

    page.get_by_role("link", name="Jobs").click()

    # TO DO: automate search for python developer
    page.goto('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')
    ul = page.inner_html("ul")
    for row in page.get_by_role("listitem").all():
        print(row.text_content())
    links = page.query_selector_all(".job-card-container--clickable")
    #page.get_by_role("button").filter(has_text="Save").click()
    print(links)



    sleep(30)

