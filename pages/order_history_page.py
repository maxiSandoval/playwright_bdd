from playwright.sync_api import Page

from .order_details_page import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self, page: Page):
        self.page = page

    def select_order(self, order_id):
        order_row = self.page.locator("tr").filter(has_text=order_id)
        order_row.get_by_role("button", name="View").click()
        order_details_page = OrderDetailsPage(self.page)
        return order_details_page