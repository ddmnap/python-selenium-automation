# Created by Дашуля at 16.12.2024
Feature: Cart Functionality

  Scenario: User can see "Your cart is empty" message
    Given I open the Target main page
    When I click on the Cart icon
    Then I should see "Your cart is empty" message


Feature: User can add a product to cart

  Scenario: User can see "Your cart is empty" message
    Given I open the Target main page
    When Search for mug
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then I should see cart has 1 item(s)