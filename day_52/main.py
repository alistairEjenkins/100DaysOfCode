from playwright.sync_api import sync_playwright
from insta_follower import InstaFollower

def main():
    with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=50)
            page = browser.new_page()
            insta_follower = InstaFollower(page)
            insta_follower.find_followers()

if __name__ == "__main__":
    main()
#<button class="_acan _acap _acas _aj1-" type="button">Save Info</button>
#<button class="_a9-- _a9_1" tabindex="0">Not Now</button>

#<input aria-label="Search input" autocapitalize="none" class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j" dir="" placeholder="Search" type="text" value="">
