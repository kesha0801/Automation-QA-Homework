from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'div[data-focusid="10805587_product_card"] [id*="addToCartButton"]')
SIDE_NAV_ADD_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
ADDED_TO_CART_HEADER = (By.XPATH, "//span[text()='Added to cart']")


@then("Click add to cart")
def add_to_cart(context):
    sleep(5) #This step won't work without sleep
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
    context.driver.wait.until(EC.element_to_be_clickable(SIDE_NAV_ADD_CART_BTN)).click()

# @then("Click add to cart")
# def add_to_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[id='addToCartButtonOrTextIdFor10805587']").click()
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
#     sleep(2)


@then("Verify cart has pencil")
def cart_has_pencil(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']")
    assert expected_text in actual_text.text




@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
