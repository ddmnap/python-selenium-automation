
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

Feature: Tests for search
  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea
  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee
  Scenario: User can search for a mug
    Given Open target main page
    When Search for a mug
    Then Verify search results shown for a mug
  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image