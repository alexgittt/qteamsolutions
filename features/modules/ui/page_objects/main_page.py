from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *

class MainPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context


    self.navbar           = self.browser.element(id="ui-id-2")
    self.bags_page        = self.browser.element(xpath=f"//div[@class='categories-menu']//ul[@class='items']//a[text()='Bags']")
    self.gear_page        = self.browser.element(class_name="base", text="Gear")


    super().__init__(self.browser, self.context)

