import sys
from playwright.sync_api import sync_playwright
def run_test(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False ,args=["--start-maximized"])
        # page = browser.new_page()
        context = browser.new_context(viewport={"width": 1960, "height": 1080})  
        page = context.new_page()
        page.goto(url)
        page.wait_for_load_state("load")
        page.locator("body > div > div > div.h-full > div > div > div.w-screen.md\:w-full.bg-base-100.md\:shadow-lg.md\:rounded-lg.md\:py-4.md\:mt-8 > h2").scroll_into_view_if_needed()
        page.click("body > div > div > div.h-full > div > div > div.w-screen.md\:w-full.bg-base-100.md\:shadow-lg.md\:rounded-lg.md\:py-4.md\:mt-8 > div > div.w-full.aspect-\[4\/3\].flex.items-center.justify-center.bg-base-200.rounded-lg.p-6 > div > a")
        
        page.wait_for_timeout(4000)
        page.fill("#phone","9000012345")
        page.click("body > div > div > div.h-full > div > div > div > div > div:nth-child(1) > form > button")
        page.fill("#otp","123456")
        page.wait_for_timeout(3000)
        page.click("body > div > div > div.h-full > div > div > div.flex.items-center.justify-center.h-3\/4.bg-teal-50.rounded-lg.border-2.border-teal-100 > div > div.space-y-2.text-center > form > button")
        page.wait_for_timeout(5000)
        page.go_back()
        page.locator("body > div > div > div.h-full > div > div > div.max-w-md.mx-auto.bg-white.md\:max-w-none.md\:shadow-none.md\:rounded-none.md\:bg-gray-50 > div.p-6.md\:p-0.md\:max-w-7xl.md\:mx-auto.md\:w-full.md\:py-4.md\:bg-gray-50 > div > div.md\:p-4.md\:rounded-lg.md\:text-card-foreground.md\:shadow-lg.md\:bg-base-100.md\:h-\[calc\(100\%\+10rem\)\].flex.flex-col.h-full > h2").scroll_into_view_if_needed()
        page.wait_for_timeout(2000)
        page.locator("#builder > div.text-xl.font-bold").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        # AIR QUALITY CHECK
        page.click("body > div > div > div.h-full > div > div > div.bg-white.p-4.rounded-xl > div")
        page.wait_for_timeout(3000)
        # FLOOR PLAN IMAGES CHECK
        page.click("body > div > div > div.h-full > div > div > div.max-w-md.mx-auto.bg-white.md\:max-w-none.md\:shadow-none.md\:rounded-none.md\:bg-gray-50 > div.p-4.md\:p-0.md\:bg-base-100.md\:shadow-md.md\:rounded-xl > div > div > div > div > div > div:nth-child(1) > a > button > svg")
        page.locator("body > div > div > div.h-full > div > div > div.col-span-1").scroll_into_view_if_needed()
        page.locator("body > div > div > div.h-full > div > div > div:nth-child(2) > div > div > div > img").scroll_into_view_if_needed()
        page.click("body > div > div > div.h-full > div > div > div:nth-child(2) > div > div > div > img")
        page.wait_for_timeout(4000) 
        page.go_back()
        # PRICING OF PROJECT
        page.locator("#project-pricing").scroll_into_view_if_needed()
        page.wait_for_timeout(3000)
        # NEAR BY PLACES
        page.locator("body > div > div > div.h-full > div > div > div:nth-child(11) > div").scroll_into_view_if_needed()
        page.wait_for_timeout(4000)
        
        browser.close()
us_url= input("please enter the url : ")
run_test(us_url)