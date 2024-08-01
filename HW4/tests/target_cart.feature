Feature: Tests for Cart functionality

#This scenario is for Homework4:
#3. Create a test case to add any Target’s product into the cart,
#and make sure it’s there (check that your cart has individual cart items OR the total price, up to you!)


  Scenario: Product is added to cart
    Given Open target main page
    When Search for pencil
    Then Click add to cart
    Then Verify cart has pencil



  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown



