Feature:  OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome Browser
    When I open orange hrm homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page
  Scenario Outline:Login to OrangeHRM with multiple parameters
    Given I launch chrome Browser
    When I open orange hrm homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
       | username | password |
       | admin    | admin123 |
       | admin123 | admin    |
       | adminxyz | admin123 |
       | admin    | adminxyz |