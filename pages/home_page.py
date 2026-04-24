from pages.login_page import LoginPage


class HomePage:
    URL = "/"

    def __init__(self, page):
        self.page = page
        self.heading = page.locator("#main-title")
        self.login_link = page.get_by_role("link", name="Test Login Page")
        self.search_input = page.locator("#search-input")
        self.search_button = page.locator("#search-button")
        self.search_results = page.locator(".col-md-3.mb-2")
        self.login_try_it_out = page.locator(".col-md-3.mb-2").filter(has_text="Test Login Page").get_by_role("link", name="Try it out")

    def navigate(self):
        self.page.goto(self.URL)

    def go_to_login(self):
        self.login_link.click()
        return LoginPage(self.page)

    def go_to_login_via_button(self):
        self.login_try_it_out.click()
        return LoginPage(self.page)

    def search(self, query):
        self.search_input.fill(query)
        self.search_button.click()
