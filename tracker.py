from dotenv import dotenv_values
from playwright.sync_api import sync_playwright
from time import sleep
from notifypy import Notify

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

# In the dotenv we must have USERNAME and PASSWORD
config = dotenv_values(".env")
page_html = ""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://scolagile.pw/")

    page.fill('input[name="username"]', str(config.get("USERNAME")))
    page.fill('input[name="password"]', str(config.get("PASSWORD")))

    page.click('input[id="kc-login"]')

    # Wait for page to finish navigation
    page.wait_for_load_state('load')
    page.goto("https://fst-scolagile.uh1.ac.ma/#/scolarite/etudiant/0/notes")
    sleep(1)
    
    # Parsing the page
    page_html = page.content()
    i = 1
    while True:
        sleep(10)
        page.goto("https://fst-scolagile.uh1.ac.ma/#/scolarite/etudiant/0/notes")
        html = page.content()
        if html != page_html:
            notification.send()
            page_html = html
            pass
        print(f"request number {i}", end="\r")
        i += 1
