Feature: Register
  Background: Common Steps
    Given launch the browser
    And open Demo Web Shop

  Scenario: Click on Register
    Then Click on Register Button
    And Select radio button for gender
    Then enter your first name
    Then enter your last name
    And enter you valid email id
    Then enter password
    And Enter confirm password
    Then click the Register Button
    Then Click on Login Button
    And Enter Valid email id
    Then Enter Valid Password
    Then Select check box for remeber me
    Then Click on Forgot Password
    And Click the Login Button
    Then Click on Logout Button




