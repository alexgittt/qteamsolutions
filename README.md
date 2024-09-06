# qteamsolutions_demo

# 1. Install and run tests on a local machine
# 2. View the allure report
# 3. Common errors


# 1. Install and run tests on a local machine

## 1.1. Install python3 your local machine
Check on the net how to install python3

## 1.2. Install the requirements
Navigate to Project directory and run the below commands to install reiquired packages

	   sudo apt install python3.11-venv
       python3 -m pip install -r requirements.txt

## 1.4. Run the tests
The tests are separate for API and UI
 - Run both API and UI tests with the command:

        behave

 - Run only API tests:

        behave --tags=api

 - Run only UI tests:

        behave --tags-ui


# 2. View the allure report 
After running the tests, an allure report HTML page is created and can be seen with the following command:

        allure serve allure-results


# 3. Common errors

##  ChromeDriver version error
SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 81

Solution 1(preffered): git pull
Drivers can be found inside the /drivers folder from the root project. 
Normally, the ChromeDriver is always updated by the automation team, so it's version is synchronied with Chrome browser version(stable one).
So, a git pull should solve the issue.

Solution 2: notify the automation team to change the chromedriver and then git pull, after they fixed it.

Solution 3: change the chromedriver locally and then push it
Chromedriver can be found here https://chromedriver.chromium.org/downloads or https://googlechromelabs.github.io/chrome-for-testing/#stable

## The chromedriver cannot be open on Mac, due to malicios error
Solution: go to the chromedriver location, right click on it and open with terminal