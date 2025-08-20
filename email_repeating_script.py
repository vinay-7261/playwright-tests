
import sys
from playwright.sync_api import sync_playwright
emails = [
    "alice.test@example.com",
    "bob.demo@example.org",
    "charlie.qa@example.net",
    "diana.user@example.com",
    "eve.sample@example.org",
    "frank.dev@example.net",
    "grace.testuser@example.com",
    "henry.form@example.org",
    "irene.bot@example.net",
    "jack.sampleuser@example.com"
]
def run_test(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set True if you want headless
        page = browser.new_page()
        page.goto(url)
        page.click("body > div > div > div.navbar.bg-white.h-20.border-b.border-base-200 > div.navbar-end > ul > li:nth-child(2) > a")
        for mail in emails:
            page.fill("#phone",mail)
            page.wait_for_timeout(2000)
            page.click("body > div > div > div.h-full > div > div > div > div > div:nth-child(1) > form > button")
            page.wait_for_timeout(2000)
            page.go_back()
            page.click("body > div > div > div.navbar.bg-white.h-20.border-b.border-base-200 > div.navbar-end > ul > li:nth-child(2) > a")


        # Just printing the title as an example
        print("Page Title:", page.title())
        page.wait_for_timeout(10000)

        browser.close()

user_url = input("plase entre url: ")
run_test(user_url)

    
