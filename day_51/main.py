from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    class InternetSpeedTwitterBot:

        def __Init__(self):
            self.page = self.set_up_page()
            self.up
            self.down

        def set_up_page(self):
            browser = p.chromium.launch(headless=False, slow_mo=50)
            page = self.browser.new_page()
            page.goto('https://www.speedtest.net/')
            time.sleep(60)
            return page

        def get_internet_speed(self):

            self.go_button = self.page.get_by_text('Go')
            self.go_button.
            self.go_button.click()

        def tweet_at_provider(self):

            pass

    speed_bot = InternetSpeedTwitterBot()
    # speed_bot.get_internet_speed()
    #speed_bot.tweet_at_provider()