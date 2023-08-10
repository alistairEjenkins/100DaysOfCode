# completed using playwright - bug in selenium

from playwright.sync_api import sync_playwright
import time

time_to_buy = time.time() + 5
time_to_stop = time.time() + 60

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://orteil.dashnet.org/experiments/cookie/')

    cookie = page.query_selector('#cookie')

    cookies_per_second = page.query_selector('#cps')

    add_ons = page.query_selector_all('.grayed')
    add_ons = add_ons[:-1]
    add_on_ids = [add_on.get_attribute('id') for add_on in add_ons]

    game_is_on = True
    while game_is_on:
        cookie.click()

        prices = page.query_selector_all("#store b")
        prices = prices[:-1]
        all_prices = [int(price.inner_text().split(' -  ')[1].replace(',', '')) for price in prices]

        money = int(page.query_selector('#money').inner_text().replace(',', ''))

        purchase_index = None
        for price in all_prices:
            if money >= price:
                purchase_index = all_prices.index(price)

        try:
            purchase = add_on_ids[purchase_index]
        except TypeError:
            pass
        else:
            purchase = page.query_selector(f'#{purchase}')
            purchase.click()
        time_to_buy = time.time() + 5

        if time.time() >= time_to_stop:
            print(f"Cookies/second: {cookies_per_second.inner_text()}")
            game_is_on = False


