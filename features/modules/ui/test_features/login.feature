Feature: UI

	@ui
	Scenario: UI: Login into account
    Given UI: I go to automation page
    When UI: I go to "Login automation" page
    Then UI: I check that Login Automation page is opened
    When UI: I login with user "admin"
    Then UI: I am logged in

