from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized", "--window-position=0,0"]
    )
    context = browser.new_context(viewport=None)  # disables fixed size
    page = context.new_page()
    page.goto("https://test.bhumiboss.com/project/5235ff8f-5d95-481e-9d78-eced8cb2ca2f?forward=null")

    # Print the actual window size to check
    size = page.evaluate("() => ({w: window.innerWidth, h: window.innerHeight})")
    print("Inner window size:", size)

    # Keep the browser open so you can see the size
    input("Press Enter to close...")
    browser.close()
