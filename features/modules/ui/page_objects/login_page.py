from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *

class LoginPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context


    self.automation_page  = self.browser.div(id="et-main-area")
    self.auto_page        = self.browser.element(href="../complicated-page")
    self.login_screen     = self.browser.element(class_name="sign-in-page")

    self.email            = self.browser.element(id="user[email]")
    self.password         = self.browser.element(id="user[password]")
    self.signin_btn       = self.browser.element(class_name="button", tag_name="button")
    self.my_dashboard     = self.browser.element(href="/enrollments") 

    self.account_dropdown = self.browser.element(class_name="dropdown__toggle-button")
    self.sign_in_btn      = self.browser.element(href="/users/sign_in")
    self.sign_out_btn     = self.browser.element(href="/users/sign_out")

    self.login_error      = self.browser.div(id="notifications").element(class_name="message-text", text="Invalid email or password.")


    super().__init__(self.browser, self.context)
