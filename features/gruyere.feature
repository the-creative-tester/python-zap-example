Feature: Gruyere

  Scenario: Gruyere
    Given I navigate to Gruyere
    When I choose to Agree & Start
    Then I am taken to "Gruyere: Home"
    
    Given I choose to Sign Up
    When I choose to Create Account with user name "blue" and password "cheese"
    Then I am taken to "Gruyere: Error"

    Given I choose to Sign In
    When I choose to Login with user name "blue" and password "cheese"
    Then I am taken to "Gruyere: Home"