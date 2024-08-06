Feature: Tests for product page

  Scenario Outline: User can select colors
    Given Open target product <product_id> page
    Then Verify user can click through colors <expected_colors>
    Examples:
    |product_id   |expected_colors                            |
    |A-91511634   |dark khaki, stone/grey, white/sand/tan     |
    |A-54551690   |Blue Tint, Denim Blue, Marine, Raven       |

