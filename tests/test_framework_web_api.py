import json
import pytest

from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from utils.api_base import ApiUtils

# json file -> utils -> access into test
with open("resources/credentials.json") as credentials_file:
    test_data = json.load(credentials_file)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]
    print(user_credentials_list)

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browser_selection ,user_credentials):
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    api_utils = ApiUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    login_page = LoginPage(browser_selection)
    login_page.navigate()
    # login_page.login(user_email, user_password)
    # dashboard_page = DashboardPage(pages)

    dashboard_page = login_page.login(user_email, user_password)
    order_history_page = dashboard_page.select_orders_nav_link()
    order_details_page = order_history_page.select_order(order_id)
    order_details_page.verify_order_message()
