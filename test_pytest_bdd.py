import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from utils.api_base import ApiUtils
from pages.login_page import LoginPage

scenarios("features/order_transaction.feature")


@pytest.fixture
def shared_data():
    return {}

# parsers.parse is used when we have variables in the step
@given(parsers.parse("place the item order with {username} and {password}"))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {"user_email": username, "user_password": password}
    api_utils = ApiUtils()
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data["order_id"] = order_id

@given("the user is on landing page")
def user_on_landing_page(browser_selection, shared_data):
    login_page = LoginPage(browser_selection)
    login_page.navigate()
    shared_data["login_page"] = login_page

@when(parsers.parse("I login to portal with {username} and {password}"))
def login_to_portal(username, password, shared_data):
    dashboard_page = shared_data["login_page"].login(username, password)
    shared_data["dashboard_page"] = dashboard_page

@when("navigate to orders page and select orderId")
def navigate_and_select_order_id(shared_data):
    order_history_page = shared_data["dashboard_page"].select_orders_nav_link()
    order_details_page = order_history_page.select_order(shared_data["order_id"])
    shared_data["order_details_page"] = order_details_page

@then("order message is successfully displayed")
def verify_success_message(shared_data):
    shared_data["order_details_page"].verify_order_message()
