from playwright.sync_api import Page
from .dashboard_page import DashboardPage

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self, user_email, user_password):
        self.page.locator("#userEmail").fill(user_email)
        self.page.locator("#userPassword").fill(user_password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self.page)
        return dashboard_page