# Created by dipes at 4/27/2022
Feature: Add to cart feature
  User should be able to add books to the cart when they log in.

  Scenario: Verify add to cart functionality
    Given Open the app for cart
    When enter the login data for cart
    Then click signin for cart
    Then verify the hpage title
    Then click the addtocart button
    Then click cart buton
    Then verify the cpage title
    Then delete the item from cart
#    Then click on onclick
    And close the cart app