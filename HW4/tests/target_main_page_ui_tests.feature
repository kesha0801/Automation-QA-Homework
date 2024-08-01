Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open Target main page
    Then Verify header in shown

  Scenario: Verify 10 benefit cells
    Given Open Target main page
    When Get all benefit cells within circle
    Then Verify benefit cells has 10 links
