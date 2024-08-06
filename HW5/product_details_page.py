from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div picture")
SELECTED_COLOR = (By.CLASS_NAME, "sc-40df79dd-1.kda-dqB")



@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(4)


@then('Verify user can click through colors {expected_colors}')
def click_and_verify_colors(context, expected_colors):
    expected_colors= expected_colors.split(', ')
    print(f" EXPECTED COLORS:  {expected_colors} {len(expected_colors)}")

    #expected_colors = ['dark khaki', 'stone/grey', 'white/sand/tan']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        sleep(5)
        color.click()

        first_component = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/VariationComponent']")[0]

        if "color" not in first_component.text.lower():
            first_component = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/VariationComponent']")[1]

        first_div = first_component.find_element(By.TAG_NAME, "div")
        select_color = first_div.text

        #select_color = context.driver.find_elements(*SELECTED_COLOR)
        #selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        selected_color = select_color.split('\n')[1]
        print(f"Color detected {selected_color}")

        actual_colors.append(selected_color)
    print(f" ACTUAL COLORS FOUND: {actual_colors}")

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'



