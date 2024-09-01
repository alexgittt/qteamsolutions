from nerodia.browser import Browser
from config.initialize_driver import initialize_driver
import os

def before_all(context):
    # Load configurations like base URL, API version, API key, etc.
    context.base_url = context.config.userdata.get('base_url')
    context.api_version = context.config.userdata.get('api_version')
    context.api_key = context.config.userdata.get('api_key')
    context.url = context.config.userdata.get('url_ui')

def before_feature(context, feature):
    if "UI" in feature.name:
        context.browser = initialize_driver(context.config.userdata.get('browser'))
        context.execute_steps(u'''given UI: Initialize Pages''')

def after_step(context, step):
    if step.status == "failed" and hasattr(context, 'browser'):
        # Take a screenshot on failure and attach it to the report
        screenshot_path = os.path.join(os.getcwd(), 'screenshots', f"{step.name}.png")
        context.browser.screenshot.save(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        # Optionally, attach the screenshot to an Allure report
        # allure.attach.file(screenshot_path, name=step.name, attachment_type=allure.attachment_type.PNG)

def after_scenario(context, scenario):
    if hasattr(context, 'browser'):
        clear_browser_state(context.browser.driver)

def after_feature(context, feature):
    if hasattr(context, 'browser'):
        context.browser.quit()
        del context.browser

def after_all(context):
    # Any global cleanup can be done here
    pass

def clear_browser_state(driver):
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
