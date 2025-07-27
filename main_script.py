from playwright.sync_api import sync_playwright
lst = ["myhome apas", "my home vipina", "aparna zenon", "elara","myhome grava"]
def run_test(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set True for headless mode
        page = browser.new_page()
        print(f"Opening site: {url}")
        page.goto(url)
        page.wait_for_load_state("networkidle")
        print("Page Title:", page.title())
        try:
            heading = page.locator("h1").first.text_content()
            print("Main Heading:", heading.strip())
        except:
            print("No <h1> tag found.")
        page.click("body > div > div > div.h-full > div > div.relative.h-\[480px\].md\:h-\[500px\] > div.relative.z-10.max-w-5xl.mx-auto.pt-20.px-4 > div > div > div > div.grid.grid-cols-1.md\:grid-cols-2.gap-4 > button")
        page.click("body > div > div > div.h-full > div > div > div > div > div > div > button:nth-child(1)")
        page.click("body > div > div > div.h-full > div > div > div > div > div > div > button:nth-child(1) > span.font-bold.text-base")
        page.click("body > div > div > div.h-full > div > div > div > div > div > div > button:nth-child(1)")
        page.click("body > div > div > div.navbar.bg-white.h-20.border-b.border-base-200 > div.navbar-end > ul > li:nth-child(1) > a > svg")

        for name in lst:
            page.fill("body > div > div > div.h-full > div > div > div > div > div > div > div > div > div > div > input",name)
            page.wait_for_timeout(2000)
            pr_name = page.locator("body > div > div > div.h-full > div > div > div > div > div > div > div.absolute.z-10.bg-white.border.border-gray-300.rounded-lg.top-full.mt-1.w-full.shadow-lg > a > div > p.ml-2.mr-1.grow.basis-8\/12.truncate.uppercase.font-semibold.text-gray-700.text-xs.md\:text-sm").inner_text()
            if name.upper() == pr_name:
                page.wait_for_timeout(2000)
                page.click("body > div > div > div.h-full > div > div > div > div > div > div > div.absolute.z-10.bg-white.border.border-gray-300.rounded-lg.top-full.mt-1.w-full.shadow-lg > a > div")
                page.locator("#builder > div.text-xl.font-bold").scroll_into_view_if_needed()
                page.wait_for_timeout(4000)
                page.locator("#project-pricing > div.text-xl.font-bold.mb-3.text-primary").scroll_into_view_if_needed()
                page.wait_for_timeout(2000)
                page.go_back()
                print("yes the prject", name, "is found")
            else:
                print("the project" , name ,"is not found")
        page.wait_for_timeout(20000)  
        
        browser.close()
user_url = input("Enter the URL of the BhumiBoss site: ")
# s_t =input("enter roject name")
run_test(user_url)

