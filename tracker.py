from dotenv import dotenv_values
from playwright.sync_api import sync_playwright
from time import sleep
from notifypy import Notify

# Checking the environment variables
# In the dotenv we must have USERNAME and PASSWORD
config = dotenv_values(".env")
if config.get("USERNAME") is None or config.get("PASSWORD") is None:
    print("The environment variables weren't setup correctly, you should define USERNAME and PASSWORD")
    exit(1)

# setting up the notification
notification = Notify()
notification.title = "The app is running"
notification.application_name = "Scolagile tracker"
notification.message = "It'll be running smoothly in the background"
notification.icon = "icon/icon.png"
notification.urgency = "critical"
notification.send()

notification.title = "Scolagile Notes Changed!!"
notification.message = "Someone changed your notes on scolagile, enter to check them"

# scraping the website
SCOLAGILE_URL = "https://scolagile.pw/"
SCOLAGILE_NOTES_URL = "https://fst-scolagile.uh1.ac.ma/#/scolarite/etudiant/0/notes"
page_html = ""

with sync_playwright() as p:
    print("Launching headless browser...")
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    print("Navigating to scolagile...")
    page.goto(SCOLAGILE_URL)

    # str here just to supress a warning
    print(f"Athenticating user {str(config.get('USERNAME'))}...")
    page.fill('input[name="username"]', str(config.get("USERNAME")))
    page.fill('input[name="password"]', str(config.get("PASSWORD")))

    page.click('input[id="kc-login"]')

    # Wait for page to finish navigation
    page.wait_for_load_state('load')
    page.goto(SCOLAGILE_NOTES_URL)

    # periodically checking the page
    print("Checking... If a change is detected you'll be notified")    
    page_html = page.content()
    i = 1
    while True:
        sleep(30)
        page.goto(SCOLAGILE_NOTES_URL)
        html = page.content()
        if html != page_html:
            notification.send()
            page_html = html
            print("The page has changed, you should take a look!!")
            pass
        print(f"request number {i}", end="\r")
        i += 1
