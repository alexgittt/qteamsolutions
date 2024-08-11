from config.config import *
from nerodia.browser import Browser
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def initialize_driver(browser):
    if browser.upper() == "CHROME" or browser.upper() == "C":
        opts = webdriver.ChromeOptions()
        opts.add_argument('ignore-certificate-errors')

        match sys.platform:
            case "darwin":
                chromedriverbinary = os.path.abspath("drivers/" + sys.platform + "/chromedriver")
                prefs = {"download": {"prompt_for_download": "false", "default_directory": os.path.abspath(downloads_dir)}}
                opts.add_experimental_option('prefs', prefs)

            case "linux":
                chromedriverbinary = os.path.abspath("drivers/" + sys.platform + "/chromedriver")
                prefs = {"download": {"prompt_for_download": "false", "default_directory": os.path.abspath(downloads_dir)}}
                opts.add_experimental_option('prefs', prefs)

            case "windows":
                chromedriverbinary = os.path.abspath("drivers/" + sys.platform + "/chromedriver.exe").replace("/", "\\")
                prefs = {"download": {"prompt_for_download": "false", "default_directory": os.path.abspath(downloads_dir).replace("/", "\\")}}
                opts.add_experimental_option('prefs', prefs)

            case _:
                raise Exception(f"Unsupported platform: {sys.platform}")
        
        service = Service(chromedriverbinary)
        chromedriver = webdriver.Chrome(service=service, options=opts)
        return Browser(chromedriver)

    if browser.upper() == "CHROMEHEADLESS" or browser.upper() == "CH":
        opts = webdriver.ChromeOptions()
        opts.add_argument('no-sandbox')
        opts.add_argument('ignore-certificate-errors')
        opts.add_argument('disable-dev-shm-usage')
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--start-maximized")
        opts.add_argument("--headless")

        match sys.platform:
            case "darwin":
                chromedriverbinary = os.path.abspath("drivers/" + sys.platform + "/chromedriver")
                prefs = {"download": {"prompt_for_download": "false", "default_directory": os.path.abspath(downloads_dir)}}
                opts.add_experimental_option('prefs', prefs)

            case "linux":
                chromedriverbinary = os.path.abspath("drivers/" + sys.platform + "/chromedriver")
                prefs = {"download": {"prompt_for_download": "false", "default_directory": os.path.abspath(downloads_dir)}}
                opts.add_experimental_option('prefs', prefs)

            case "windows":
                chromedriverbinary = os.path.abspath("drivers/" + sys.platform + "/chromedriver.exe").replace("/", "\\")
                prefs = {"download": {"prompt_for_download": "false", "default_directory": os.path.abspath(downloads_dir).replace("/", "\\")}}
                opts.add_experimental_option('prefs', prefs)

            case _:
                raise Exception(f"Unsupported platform: {sys.platform}")
        
        service = Service(chromedriverbinary)
        chromedriver = webdriver.Chrome(service=service, options=opts)
        return Browser(chromedriver)

    # Other browsers
    if browser.upper() == "FIREFOX" or browser.upper() == "FF" or browser.upper() == "F":
        return

    if browser.upper() == "INTERNET EXPLORER" or browser.upper() == "IE" or browser.upper() == "I":
        return

    if browser.upper() == "SAFARI" or browser.upper() == "S":
        return

    if browser.upper() == "OPERA" or browser.upper() == "O":
        return

    if browser.upper() == "PHANTOMJS" or browser.upper() == "PHANTOM" or browser.upper() == "P":
        return

    raise Exception(f'Cannot initialize the driver for browser "{browser.upper()}"')
