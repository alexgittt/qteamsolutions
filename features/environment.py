# from config.initialize_driver import *
from PIL import Image
import datetime
import allure
import io
import os


def before_all(context):
    context.base_url = context.config.userdata.get('base_url')
    context.api_version = context.config.userdata.get('api_version')
    context.api_key = context.config.userdata.get('api_key')

   

def before_feature(context, feature):
    context.feature.timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # if "Hyper-API" in feature.name:
    #     context.config.cookies = {}

    #     if context.config.sut_file["primary"]["syneto"]["ip"] != "":
    #         context.execute_steps(u'''given API - Auth: Get cookies for "{machine}" machine'''.format(machine="primary"))
        
    #     if context.config.sut_file["secondary"]["syneto"]["ip"] != "":
    #         context.execute_steps(u'''given API - Auth: Get cookies for "{machine}" machine'''.format(machine="secondary"))
        
    #     if context.config.sut_file["backup"]["syneto"]["ip"] != "":
    #         context.execute_steps(u'''given API - Auth: Get cookies for "{machine}" machine'''.format(machine="backup"))
    
    #     return

    # if "Hyper-UI" in feature.name:
    #     context.driver = initialize_driver(context.config.userdata['BROWSER'])

    #     if 'SYNETO_OS_IP' in context.config.userdata and context.config.userdata['SYNETO_OS_IP'] != '':
    #         context.config.ui_syneto_url = context.config.userdata['SYNETO_OS_IP']
    #         print("SYNETO_OS_IP: Syneto URL For UI: ", context.config.ui_syneto_url)
    #     else:
    #         context.config.ui_syneto_url = context.config.url['secondary']['syneto']
    #         print("Secondary: Syneto URL For UI: ", context.config.ui_syneto_url)
        
    #     if "Quick Setup" not in feature.name:
    #         context.execute_steps(u'''given UI: Log in as "{user}"'''.format(user="admin"))
    #     else:
    #         context.execute_steps(u'''given UI: Initialize Pages''')
    #     return


def after_step(context, step):
    if step.status == "failed" or step.status == 'broken':

        # Only for 'UI' tests. On 'API' tests driver is not initialized
        screenshot_can_be_taken = hasattr(context, 'driver')

        if screenshot_can_be_taken:
            screenshot_path = 'last_screenshot.png'

            # Capture the screenshot as a PIL.Image object
            try:
                byteImgIO = io.BytesIO(context.driver.screenshot.save(screenshot_path))
                screenshot = Image.open(screenshot_path)
                screenshot.save(byteImgIO, "PNG")
                byteImgIO.seek(0)
                byteImgIO.read()  # Check screenshot is taken: this will throw when image is not written properly

            except Exception as e:
                print("Error taking screenshot:", e)
                return

            # Attach the screenshot to the Allure report
            with allure.step('Take a screenshot'):
                allure.attach.file(screenshot_path, name=step.name, attachment_type=allure.attachment_type.PNG)


def after_scenario(context, any):
    if hasattr(context, 'driver'):
        context.driver.goto(context.config.ui_syneto_url)
    return context


def after_feature(context, feature):
    print(context)

    if hasattr(context, 'driver'):
        context.driver.quit()
    return context
