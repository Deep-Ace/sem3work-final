# Created by dipes at 4/27/2022
Feature: Test the BookMart application
    Scenario: Verify register functionality
        Given Launch the Register App
        When enter the register credentials
        Then click terms
        Then click register
        Then verify the rpage title
        And close the Register App