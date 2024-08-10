from nerodia.browser import Browser
from config.initialize_driver import *
import os

def before_all(context):
    # Load configurations like base URL, API version, API key, etc.
    context.base_url = context.config.userdata.get('base_url')
    context.api_version = context.config.userdata.get('api_version')
    context.api_key = context.config.userdata.get('api_key')
    context.url = context.config.userdata.get('url_ui')

def before_feature(context, feature):

    if "UI" in feature.name:
        context.driver = initialize_driver(context.config.userdata.get('browser'))
        context.execute_steps(u'''given UI: Initialize Pages''')

        return


def after_step(context, step):
    if step.status == "failed" and hasattr(context, 'browser'):
        # Take a screenshot on failure and attach it to the report
        screenshot_path = os.path.join(os.getcwd(), 'screenshots', f"{step.name}.png")
        context.browser.screenshot.save(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        # Optionally, attach the screenshot to an Allure report
        # allure.attach.file(screenshot_path, name=step.name, attachment_type=allure.attachment_type.PNG)

# def after_feature(context, feature):
#     if hasattr(context, 'browser'):
#         # Close the browser after each feature
#         context.browser.quit()

def after_feature(context, feature):

    if hasattr(context, 'driver'):
        context.driver.quit()
    return context

def after_all(context):
    # Any global cleanup can be done here
    pass