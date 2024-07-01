# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://ma.indeed.com/")
#     page4 = context.new_page()
#     page4.goto("https://ma.indeed.com/viewjob?cmp=Profficiis&t=D%C3%A9veloppeur+Full+Stack&jk=eea6ab1df9005603&xpse=SoDv67I3_3m0dwZOnZ0LbzkdCdPP&xfps=1b037277-9ca2-4751-9e80-11ef943ee434&xkcb=SoC367M3_3m46xgpAr0LbzkdCdPP&vjs=3")
#     page4.get_by_label("Apply now").click()
#     page4.get_by_role("button", name="Continue").click()
#     page4.get_by_role("heading", name="Enter a past job that shows").click()
#     page4.get_by_text("Relevant experience", exact=True).click()
#     page4.get_by_test_id("9523bccb784382df94fc894afdbec04485ffbb1f29311511e6dc6bcedcc58d1c").click()
#     page4.get_by_role("heading", name="Answer these questions from").click()
#     page4.get_by_text("To save time, we may start").click()
#     page4.get_by_test_id("9523bccb784382df94fc894afdbec04485ffbb1f29311511e6dc6bcedcc58d1c").click()
#     page4.get_by_test_id("input-q_34968def63e3f1d9500ebf1ed81e3dd8").press("ControlOrMeta+f")
#     page4.locator("label").filter(has_text="Oui").click()
#     page4.get_by_label("Non").check()
#     page4.get_by_label("Oui").check()
#     page4.get_by_test_id("9523bccb784382df94fc894afdbec04485ffbb1f29311511e6dc6bcedcc58d1c").click()
#     page4.get_by_role("button", name="Submit your application").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
