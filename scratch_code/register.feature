Feature: Register account functionality

  @Register
  Scenario: Register with mandatory fields
    Given I navigated to register page
    When I enter mandatory fields
    And I click on Continue button
    Then Account should get created

  @Register
  Scenario: Register with all fields
    Given I navigated to register page
    When I enter all fields
    And I click on Continue button
    Then Account should get created

  @Register
  Scenario: Register with duplicate email
    Given I navigated to register page
    When I enter all details except email
    And I click on Continue button
    Then Proper warning message about duplicate account should display

  @Register
  Scenario: Register without providing any details
    Given I navigated to register page
    When I do not enter any details
    And I click on Continue button
    Then Proper warning message for all mandatory fields should display