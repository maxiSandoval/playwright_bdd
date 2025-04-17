import time

from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page: Page):
    # iphone X, nokia edge -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign in").click()
    # filter allow us to find a specific elemnt
    iphone_product = page.locator("app-card.col-lg-3.col-md-6.mb-3").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card.col-lg-3.col-md-6.mb-3").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    # By partial text
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_ui_checks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

# To handle new pages
def test_child_window_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Performs action and waits for a popup `Page`.
    with page.expect_popup() as new_page_info:
        # new pages by clicking the element
        page.locator(".blinkingText").click()
        # get the new pge by value property
        child_page = new_page_info.value
        # get text from element
        red_text = child_page.locator(".red").text_content()
        print(red_text)
        # this will return an array
        words = red_text.split("at ")
        email = words[1].split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"

def test_handle_alert_boxes(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # lambda is a keyword used to create anonymous functions
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

def test_handle_iframe(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

def test_handle_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    price_col_value = 0
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0 :
            price_col_value = index
            print(f"Price column value is: {price_col_value}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    rice_price = rice_row.locator("td").nth(price_col_value)
    expect(rice_price).to_have_text("37")

def test_handle_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()