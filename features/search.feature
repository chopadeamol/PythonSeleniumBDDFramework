Feature:Search functionality

  @search
  Scenario: Search for a valid product
    Given I am navigated to home page
    When I entered valid product say "HP" into the search box field
    And I click on search button
    Then Valid product should get displayed in search result

  @search
  Scenario: Search for an invalid product
    Given I am navigated to home page
    When I entered Invalid product say "Hero" into the search field
    And I click on search button
    Then Proper message should displayed in search result

  @search
  Scenario: Search without entering in any product
    Given I am navigated to home page
    When I did not enter anything in text box
    And I click on search button
    Then Proper message should displayed in search result