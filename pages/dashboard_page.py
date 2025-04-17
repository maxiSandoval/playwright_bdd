from playwright.sync_api import Page

from .order_history_page import OrderHistoryPage


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def select_orders_nav_link(self):
        self.page.get_by_role("button", name="orders").click()
        order_history_page = OrderHistoryPage(self.page)
        return  order_history_page