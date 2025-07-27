from playwright.sync_api import sync_playwright
user_ip = input()

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://bhumiboss-git-main-abhi-projects.vercel.app/")  
        
        page.click("body > div > div > div.h-full > div > div.relative.h-\\[480px\\].md\\:h-\\[500px\\] > div.relative.z-10.max-w-5xl.mx-auto.pt-20.px-4 > div > div > div > div > a > button")
        page.click("body > div > div > div.h-full > div > div.mx-4.md\:mx-auto.md\:max-w-6xl.pt-10 > div > div.grid.grid-cols-1.md\:grid-cols-2.lg\:grid-cols-3.gap-6.pb-4 > div:nth-child(1) > div > div.p-3.bg-white > a")
        # page.click("body > div > div > div.h-full > div > div > div > div:nth-child(1) > div.p-4 > div > a > button")
        # page.click("body > div > div > div.navbar.bg-white.h-20.border-b.border-base-200 > div.navbar-start > ul > li:nth-child(1) > a")
        page.click("body > div > div > div.navbar.bg-white.h-20.border-b.border-base-200 > div.navbar-end > ul > li:nth-child(1) > a > svg")
        page.fill("body > div > div > div.h-full > div > div > div > div > div > div > div > div > div > div > input ", "my home apas")
        page.wait_for_timeout(3000)
        page.click("body > div > div > div.h-full > div > div > div > div > div > div > div.absolute.z-10.bg-white.border.border-gray-300.rounded-lg.top-full.mt-1.w-full.shadow-lg")
        page.fill("body > div > div > div.h-full > div > div > div > div > div > div > div > div > div > div > input",user_ip)

    
        page.wait_for_timeout(20000)

        browser.close()

test_login()
