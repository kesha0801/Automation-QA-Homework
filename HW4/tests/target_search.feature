Feature: Target main page search tests


  Scenario: User can search for fan
    Given Open target main page
    When Search for fan
    Then Verify search results shown for fan
    Then Verify correct search results URL opens for fan

  # Make sure scenario names are unique:

  Scenario: User can search for a pen
    Given Open target main page
    When Search for pen
    Then Verify search results shown for pen
    Then Verify correct search results URL opens for pen

  Scenario: User can search for an table
    Given Open target main page
    When Search for table
    Then Verify search results shown for table
    And Verify correct search results URL opens for table

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <expected_result>
    And Verify correct search results URL opens for <expected_result>
    Examples:
    |product  |expected_result    |
    |fan      |fan                |
    |pen      |pen                |
    |table    |table              |