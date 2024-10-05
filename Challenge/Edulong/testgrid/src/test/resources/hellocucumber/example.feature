Feature: An example

  Scenario: Successful Login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard

  Scenario Outline: Login With different input data
    Given the user is on the login page
    When the user enters "<username>" and "<password>"
    Then the user is redirected to the dashboard
    Examples:
      | username  | password      |
      | admin     | Admin123      |
      | superuser | superuser123  |
