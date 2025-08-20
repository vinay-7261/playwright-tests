import sys
from playwright.sync_api import sync_playwright
def run_test(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False ,args=["--start-maximized"])
        # page = browser.new_page()
        context = browser.new_context(viewport={"width": 1920, "height": 1080})  
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state("load")

        page.locator("body > div > div > div.h-full > div > div > div.w-screen.md\:w-full.bg-base-100.md\:shadow-lg.md\:rounded-lg.md\:py-4.md\:mt-8").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        page.locator("body > div > div > div.h-full > div > div > div.w-screen.md\:w-full.bg-base-100.md\:shadow-lg.md\:rounded-lg.md\:py-4.md\:mt-8 > div > div.w-full.aspect-\[4\/3\].flex.items-center.justify-center.bg-base-200.rounded-lg.p-6 > div > a").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        page.locator("body > div > div > div.h-full > div > div > div.max-w-md.mx-auto.bg-white.md\:max-w-none.md\:shadow-none.md\:rounded-none.md\:bg-gray-50 > div.p-6.md\:p-0.md\:max-w-7xl.md\:mx-auto.md\:w-full.md\:py-4.md\:bg-gray-50 > div > div.md\:p-4.md\:rounded-lg.md\:text-card-foreground.md\:shadow-lg.md\:bg-base-100.md\:h-\[calc\(100\%\+10rem\)\].flex.flex-col.h-full > h2").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        page.locator("#builder > div.text-xl.font-bold").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        # amenities_text = page.locator("text=Amenities Area").locator("xpath=../following-sibling::*").first.text_content()
        # print(amenities_text)
        page.wait_for_timeout(2000)
        page.locator("body > div > div > div.h-full > div > div > div.container.mx-auto.py-4 > div > div:nth-child(1) > h2").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        page.locator("body > div > div > div.h-full > div > div > div.container.mx-auto.py-4 > div > div.stats.shadow-sm > div > div.stat-title").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        page.click("body > div > div > div.navbar.bg-white.h-20.border-b.border-base-200 > div.navbar-end > ul > li:nth-child(2) > a")
        page.wait_for_timeout(3000)
        page.fill("#phone","alice@gmail.com")
        page.wait_for_timeout(3000)
        page.click("body > div > div > div.h-full > div > div > div > div > div:nth-child(1) > form > button")
        page.wait_for_timeout(3000)
        page.go_back()
        page.wait_for_timeout(3000)
        
        # FLOOR PALN PAGE
        page.locator("body > div > div > div.h-full > div > div > div.max-w-md.mx-auto.bg-white.md\:max-w-none.md\:shadow-none.md\:rounded-none.md\:bg-gray-50 > div.p-4.md\:p-0.md\:bg-base-100.md\:shadow-md.md\:rounded-xl > div > h3").scroll_into_view_if_needed()
        page.wait_for_timeout(2000)
        page.click("body > div > div > div.h-full > div > div > div.max-w-md.mx-auto.bg-white.md\:max-w-none.md\:shadow-none.md\:rounded-none.md\:bg-gray-50 > div.p-4.md\:p-0.md\:bg-base-100.md\:shadow-md.md\:rounded-xl > div > div > div > div > div > div:nth-child(1) > a > button")
        page.wait_for_timeout(2000)
        # page.locator("body > div > div > div.h-full > div > div > div.col-span-1 > div.grid.grid-cols-4.md\:grid-cols-6.gap-4.mt-8").scroll_into_view_if_needed()
        page.locator("body > div > div > div.h-full > div > div > div.col-span-1").scroll_into_view_if_needed()
        page.wait_for_timeout(2000)
        page.locator("body > div > div > div.h-full > div > div > div.col-span-2").scroll_into_view_if_needed()
        page.wait_for_timeout(2000)
        page.locator("body > div > div > div.h-full > div > div > div.col-span-2 > div > div > div").scroll_into_view_if_needed()
        page.click("body > div > div > div.h-full > div > div > div.col-span-2 > div > div > div > a > button")
        page.go_back()
        # FOR WHAT's APP
        page.click("body > div > div > footer > div.mx-6.text-center > div > div:nth-child(4) > a > img")
        page.wait_for_timeout(2000)
        page.go_back()
        browser.close()
user_url = input("plase entre url: ")
run_test(user_url)


        
    
