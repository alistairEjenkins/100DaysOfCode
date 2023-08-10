from time import sleep

SIMILAR_ACCOUNT = "williamshatner"
USERNAME = "alistairjenkins828"
PASSWORD = "AlexJackGeo3"

class InstaFollower:

    def __init__(self, page):

        self.page = page
        self.login()
    def login(self):

        # goto instagram page
        self.page.goto('https://www.instagram.com')
        # allow cookies
        self.page.get_by_role("button", name="Allow all cookies").click()
        sleep(5)

        # login
        self.page.get_by_label("Phone number, username, or email").fill(USERNAME)
        self.page.get_by_label("Password").filter(has_not_text="Show").fill(PASSWORD)
        self.page.get_by_role("button", name="Log in", exact=True).click()

        # save login details
        sleep(5)
        self.page.get_by_role("button", name="Save Info").click()

        # notifications
        sleep(5)
        self.page.get_by_role("button", name="Not now").click()


    def find_followers(self):

        sleep(5)
        self.page.get_by_role("link").filter(has_text="Search").click()

        sleep(5)
        self.page.get_by_placeholder("Search").fill(f"{SIMILAR_ACCOUNT}")

        sleep(5)
        self.page.get_by_role("link").filter(has_text=f"{SIMILAR_ACCOUNT}").click()
        sleep(30)

    def follow(self):

        pass

