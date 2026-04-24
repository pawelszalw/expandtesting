from pages.home_page import HomePage
from playwright.sync_api import expect

def test_page_title(page):
    home = HomePage(page)
    home.navigate()
    assert "Automation Testing Practice" in page.title()

def test_main_heading(page):
    home = HomePage(page)
    home.navigate()
    expect(home.heading).to_be_visible()
