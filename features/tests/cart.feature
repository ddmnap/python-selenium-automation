# Created by Дашуля at 16.12.2024
Feature: Cart Functionality

  Scenario: User can see "Your cart is empty" message
    Given I open the Target main page
    When I click on the Cart icon
    Then I should see "Your cart is empty" message