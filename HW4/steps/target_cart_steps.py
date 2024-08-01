from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then("Click add to cart")
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id='addToCartButtonOrTextIdFor10805587']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(2)


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