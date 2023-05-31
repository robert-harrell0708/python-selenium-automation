# Created by rharrell at 5/30/2023
Feature: Amazon Sign In Verification


  Scenario: Logged out user sees Sign In header when clicking on Returns and Orders
    Given Open amazon main page
    When Clicking on Returns and Orders
    Then Verify Sign In header on page

  Scenario: Logged out users sees Email input field when clicking on Returns and Orders
    Given Open amazon main page
    When Clicking on Returns and Orders
    Then Verify Email input field on page