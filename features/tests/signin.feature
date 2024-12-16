# Created by Дашуля at 16.12.2024
Feature: Sign-In Functionality

  Scenario: Logged-out user can navigate to the Sign-In form
    Given I open the Target website
    When I click on the Sign In button
    And I click on the Sign In from the side menu
    Then I should see the Sign In form