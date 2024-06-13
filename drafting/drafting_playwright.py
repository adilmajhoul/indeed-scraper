# from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, sync_playwright, expect

# Replace these with your Indeed credentials
USERNAME = "your-email@example.com"
PASSWORD = "your-password"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False, args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://secure.indeed.com/auth")

    page.wait_for_timeout(7000)

    page.get_by_label("Email address *").click()

    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Continue with Google").click()
    page1 = page1_info.value

    page1.get_by_label("Email or phone").click()
    page1.get_by_label("Email or phone").fill("sir.adilmajhoul@gmail.com")
    page1.get_by_role("button", name="Next").click()

    page1.get_by_label("Enter your password").click()
    page1.get_by_label("Enter your password").fill("googleskhon1-")
    page1.get_by_role("button", name="Next").click()

    page.wait_for_timeout(10000)

    page.goto(
        "https://ma.indeed.com/viewjob?cmp=WB%2526C--SMARTEEZ&t=Ing%C3%A9nieur+Informatique&jk=1d4ec57438dc725f&q=python&xpse=SoBl67I3_D7FDk2YJ50LbzkdCdPP&xfps=c0d2af31-1256-4910-b742-742ddb317ced&xkcb=SoAe67M3_D7Il_XQ7x0CbzkdCdPP&vjs=3"
    )
    page.get_by_label("Apply now").click()

    page.wait_for_timeout(10000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
