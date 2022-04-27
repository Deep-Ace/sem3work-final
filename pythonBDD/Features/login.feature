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

  Scenario: Verify logout functionality
    Given Open the App
    When enter the login data
    Then click signin
    Then verify the lpage title
    Then click the profile icon
    Then click logout
    And close the log app
