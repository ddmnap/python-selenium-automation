# Created by Дашуля at 17.12.2024
Feature: Verify Target Circle Benefits

  Scenario: Verify there are at least 10 benefit cells on the Target Circle page
    Given I open the Target Circle page
    When I count the number of benefit cells
    Then I should find at least 10 benefit cells