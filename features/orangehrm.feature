Feature:  OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home Page
    Given launch Chrome Browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser