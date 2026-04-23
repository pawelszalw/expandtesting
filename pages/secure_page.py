class SecurePage:
    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Secure Area page for Automation Testing Practice")
