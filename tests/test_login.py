import os
from dotenv import load_dotenv
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

load_dotenv()


def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login(os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD"))
    assert page.url.endswith("/secure")
    expect(login.success_message).to_be_visible()
    secure = SecurePage(page)
    expect(secure.heading).to_be_visible()

def test_invalid_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login(os.getenv("VALID_USERNAME"), "invalid_pass")
    expect(login.error_message).to_contain_text("Your password is invalid!")

def test_invalid_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("invalid_user", os.getenv("VALID_PASSWORD"))
    expect(login.error_message).to_contain_text("Your username is invalid!")

def test_invalid_login_and_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("invalid_user", "invalid_pass")
    expect(login.error_message).to_contain_text("Your username is invalid!")
