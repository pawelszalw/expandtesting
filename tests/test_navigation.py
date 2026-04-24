from playwright.sync_api import expect
from pages.home_page import HomePage


def test_navigate_to_login_via_link(page):
    home = HomePage(page)
    home.navigate()
    home.go_to_login()
    assert page.url.endswith("/login")

def test_navigate_to_login_via_button(page):
    home = HomePage(page)
    home.navigate()
    home.go_to_login_via_button()
    assert page.url.endswith("/login")

def test_navigate_to_login_through_search(page):
    home = HomePage(page)
    home.navigate()
    home.search("Test Login Page")
    expect(home.search_results).to_have_count(1)
