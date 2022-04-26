Feature: Test the BookMart application
  Scenario: Verify Home Page
    Given Launch the browser
    Then verify the page title
    And close the browser

  Scenario: Verify login functionality
    Given Launch the App
    When enter the login credentials
    Then click login
    Then verify the page title
    And close the App