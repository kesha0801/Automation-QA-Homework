

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@when('Get all benefit cells within circle')
def get_all_benefit_cells(context):
    context.driver.find_elements(By.CSS_SELECTOR, 'div[class="cell-item-content"]')
    sleep(2)


@then('Verify benefit cells has {number} links')
def verify_benefit_cells_amount(context, number):
    total_cells = context.driver.find_elements(By.CSS_SELECTOR, 'div[class="cell-item-content"]')
    count = len(total_cells)
    assert count == int(number), f"Expected 10 benefit, got {len(total_cells)}"


# @then('Verify {number} benefit cells')
# def verify_benefit_cells(context, number):
#     context.driver.find_elements(By.CSS_SELECTOR, 'div[class="cell-item-content"]')
#     sleep(5)
#     total_cells = context.driver.find_elements(By.CSS_SELECTOR, 'div[class="cell-item-content"]')
#     count = len(total_cells)
#     assert count == int(number), f'Expected {number} cells but got {count}'

    # Make sure to always assert len() for multiple elements as shown above
    # because .find_elements() function never fails.
    # This code with incorrect locator will always pass:
    #context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")