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
        page.locator("#pricing > div.mt-6.flex.flex-col.lg\:flex-row.gap-8.lg\:gap-4.justify-center.items-stretch.mx-4.lg\:mx-0 > div.relative.bg-white.rounded-2xl.shadow-md.flex-1.max-w-sm.mx-auto.flex.flex-col.border.border-primary.ring-2.ring-primary.scale-105.z-10 > div.p-5.flex.flex-col.flex-1").scroll_into_view_if_needed()
        page.wait_for_timeout(10000)
        page.click("#pricing > div.mt-6.flex.flex-col.lg\:flex-row.gap-8.lg\:gap-4.justify-center.items-stretch.mx-4.lg\:mx-0 > div.relative.bg-white.rounded-2xl.shadow-md.flex-1.max-w-sm.mx-auto.flex.flex-col.border.border-primary.ring-2.ring-primary.scale-105.z-10 > div.p-5.flex.flex-col.flex-1 > button")
        page.wait_for_timeout(10000)
        page.fill("#phone","9000012345")
        page.wait_for_timeout(4000)
        page.click("body > div > div > div.h-full > div > div > div > div > div:nth-child(1) > form > button")
        page.wait_for_timeout(5000)
        page.fill("#otp","123456")
        page.wait_for_timeout(3000)
        page.click("body > div > div > div.h-full > div > div > div.flex.items-center.justify-center.h-3\/4.bg-teal-50.rounded-lg.border-2.border-teal-100 > div > div.space-y-2.text-center > form > button")
        page.wait_for_timeout(20000)
        # page.get_by_role("button", name ="Continue").click()
        page.close()
user_url = input("plase entre url: ")
run_test(user_url)

