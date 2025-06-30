from dotenv import dotenv_values
from playwright.sync_api import sync_playwright
from time import sleep
from bs4 import BeautifulSoup
from utils.trackerUtils import *

# Checking the environment variables
# In the dotenv we must have USERNAME and PASSWORD
config = dotenv_values(".env")
if config.get("USERNAME") is None or config.get("PASSWORD") is None:
    print("The environment variables weren't setup correctly, you should define USERNAME and PASSWORD")
    exit(1)


def track(username: str, password: str):

    send_init_notification()

    # scraping the website
    SCOLAGILE_URL = "https://scolagile.pw/"
    SCOLAGILE_NOTES_URL = "https://fst-scolagile.uh1.ac.ma/#/scolarite/etudiant/0/notes"
    original_page = ""

    with sync_playwright() as p:
        print("Launching headless browser...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to scolagile...")
        page.goto(SCOLAGILE_URL)

        # str here just to supress a warning
        print(f"Athenticating user {username}...")
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        page.click('input[id="kc-login"]')

        # Wait for page to finish navigation
        page.wait_for_load_state('load')
        page.goto(SCOLAGILE_NOTES_URL)
        sleep(5)

        # periodically checking the page
        print("Checking... If a change is detected you'll be notified")    
        original_notes = get_notes(page.content())

        i = 1
        while True:
            sleep(25)
            page.reload()
            sleep(5)
            new_notes =  get_notes(page.content())
            if not compare_notes(original_notes, new_notes):
                send_change_notification()
                original_page = new_notes
                print("The page has changed, you should take a look!!")
            print(f"request number {i}", end="\r")
            i += 1


if __name__ == "__main__":
    username = str(config.get("USERNAME"))
    password = str(config.get("PASSWORD"))

    track(username, password)