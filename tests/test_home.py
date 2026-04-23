from pages.home_page import HomePage


def test_page_title(page):
    home = HomePage(page)
    home.navigate()
    assert "Automation Testing Practice" in page.title()


def test_main_heading(page):
    home = HomePage(page)
    home.navigate()
    assert home.heading.is_visible()
