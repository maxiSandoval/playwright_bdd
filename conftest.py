import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="chrome, firefox, edge, safari"
    )

@pytest.fixture
def browser_selection(playwright: Playwright, request):
    browser_name = request.config.getoption("--browser_name")
    browser = ""

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()