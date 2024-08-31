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

    def go_to_main_category(self, product_category):
        self.navigation_menu = self.browser.div(id="store.menu")
        link = self.navigation_menu.element(xpath=f"//li[contains(@class, 'category-item') and .//span[text()={product_category}]]").wait_until(method=lambda el: el.present, timeout=10)
        link.click()

    def go_to_sub_category(self, sub_category):
        self.sub_category_list = self.browser.div(class_name="sidebar")
        link = self.sub_category_list.element(xpath=f"//dl[@class='options']//a[text()={sub_category}]").wait_until(method=lambda e: e.present, timeout=10)
        link.click()

    def hover_on_category(self, category):
        self.navigation_menu = self.browser.div(id="store.menu")
        self.navigation_menu.element(xpath=f"//li[contains(@class, 'category-item') and .//span[text()={category}]]").wait_until(method=lambda el: el.present, timeout=10)

    def verify_that_element_is_displayed(self, displayed_element):
        displayed_element.wait_until(method=lambda e: e.present, timeout=20)
        assert displayed_element.present and displayed_element.visible, f"Element '{displayed_element}' not found"

    def verify_that_page_product_is_displayed(self, product_page):
        self.title_page_parent = self.browser.element(id="maincontent")
        page = self.title_page_parent.element(xpath=f"//div[@class='page-title-wrapper'][h1/span[text()={product_page}]]")
        assert page.present , f"Page '{product_page}' not visible"
    
    
