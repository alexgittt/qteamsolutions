from features.modules.ui.page_objects.browser_content import *

class BasePage(BrowserContent):
    def __init__(self, browser, context):
        self.browser = browser
        self.context = context
		
    def go_to_url(self, url):
        self.browser.goto(url)

    def click_on_element(self, element_el):
        element_el.wait_until(method=lambda el: el.present, timeout=10)
        element_el.click()

    def click_on_link(self, link_name):
        link = self.browser.link(text=link_name).wait_until(method=lambda el: el.present & el.enabled, timeout=10)
        link.click()

    def verify_that_element_is_displayed(self, displayed_element):
        displayed_element.wait_until(method=lambda e: e.present, timeout=20)
        assert displayed_element.present and displayed_element.visible, f"Element '{displayed_element}' not found"