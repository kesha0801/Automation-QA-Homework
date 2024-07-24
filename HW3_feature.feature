# Created by Bunny at 2024-07-23
Feature: Target cart icon tests

  Scenario: “Your cart is empty” message is shown
    Given Open target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: User can navigate to sign in after logging out
    Given Open target main page
    When Click on sign in
    Then From right side navigation menu click Sign In
    Then Verify Sign In form opened








