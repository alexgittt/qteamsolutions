Feature: UI

	@ui
	Scenario: UI: The user can log in into account
    Given UI: I go to automation page
    When UI: I go to "Login automation" page
    Then UI: I check that Login Automation page is opened
    When UI: I login with user "admin"
    Then UI: I am logged in

    @ui
	Scenario: UI: The user can log out
    Given UI: I go to automation page
    When UI: I go to "Login automation" page
    Then UI: I am logged in
    When UI: I log out
    Then UI: I am logged out