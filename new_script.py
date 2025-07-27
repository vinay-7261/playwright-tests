from playwright.sync_api import sync_playwright
p= sync_playwright().start()
browser = p.chromium.launch(headless =False)
page = browser.new_page()
page.goto("https://bhumiboss-git-main-abhi-projects.vercel.app/")



page.get_by_role("link", name="Sign-in").click()
page.fill()
page.wait_for_timeout(10000)
