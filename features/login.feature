Feature: Login functionality

  @login @pom
  Scenario: Login with valid credentials
    Given I navigated to login page
    When I entered valid email and password
    And I click on login button
    Then I should get login

  @login
  Scenario: Login with Invalid email and valid password
    Given I navigated to login page
    When I entered invalid email and valid password
    And I click on login button
    Then I should get proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I entered valid email and invalid password
    And I click on login button
    Then I should get proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I entered invalid email and invalid password
    And I click on login button
    Then I should get proper warning message

  @login
  Scenario: Login with without entering any credentials
    Given I navigated to login page
    When I do not enter anything in the email and password fields
    And I click on login button
    Then I should get proper warning message