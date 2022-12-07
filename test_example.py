from playwright.sync_api import Page
def test_first(page: Page):
    page.goto("https://google.com")