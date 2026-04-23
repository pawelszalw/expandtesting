class HomePage:
    URL = "/"

    def __init__(self, page):
        self.page = page
        self.heading = page.locator("#main-title")

    def navigate(self):
        self.page.goto(self.URL)
