from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(1)

@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    h1_element = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    actual_text = h1_element.text
    print(f'Actual text: {actual_text}')
    assert expected_text in actual_text, f'Expected "{expected_text}" to be in actual "{actual_text}"'
    sleep(1)

@when('Click on sign in')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(2)

@then('From right side navigation menu click Sign In')
def click_right_side(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign into your Target account'
    h1_span_element = context.driver.find_element(By.XPATH, "//h1/span[text()='Sign into your Target account']")
    actual_text = h1_span_element.text
    print(f'Actual text: {actual_text}')
    assert expected_text in actual_text, f'Expected "{expected_text}" to be in actual "{actual_text}"'
    sleep(1)



