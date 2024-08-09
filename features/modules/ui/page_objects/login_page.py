from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *

class LoginPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context

    # AboutPage elements
    self.automation_page  = self.browser.div(id="et-main-area")
    self.auto_page        = self.browser.element(href="../complicated-page")
    self.login_screen     = self.browser.element(class_name="sign-in-page")

    self.email            = self.browser.element(id="user[email]")
    self.password         = self.browser.element(id="user[password]")
    self.signin_btn       = self.browser.element(class_name="button", tag_name="button")
    self.my_dashboard     = self.browser.element(href="/enrollments")  


    # # Central elements
    # self.central_header        = self.about_page_id.h5(text="Central")
    # self.go_to_central_link    = self.about_page_id.element(href="https://central.syneto.eu")
    # self.unlink                = self.about_page_id.element(class_name='unlink', tag_name='gt-button')

    # # Unlink confirm modal
    # self.unlink_confirm        = self.browser.div(class_name='modal-content')
    # self.unlink_confirm_modal  = self.unlink_confirm.h5(text="Confirm")

    # # Software elements
    # self.software_header       = self.about_page_id.h5(text="Software")
    # self.version               = self.about_page_id.h6(text="Version")
    # self.version_value         = self.version.parent(tag_name="td")
    # self.last_boot             = self.about_page_id.h6(text="Last boot")
    # self.up_time               = self.about_page_id.h6(text="Uptime")

    # # Hardware elements
    # self.hardware_header       = self.about_page_id.h5(text="Hardware")
    # self.serial_number         = self.about_page_id.h6(text="Serial number")
    # self.serial_number_value   = self.serial_number.parent(tag_name="td")
    # self.processor             = self.about_page_id.h6(text="Processor")
    # self.memory                = self.about_page_id.h6(text="Data drives")
    # self.network               = self.about_page_id.h6(text="Network")

    # # Central page
    # self.central_page          = self.browser.div(id="root")
    # self.central_box           = self.central_page.h5(text="Syneto Central")






    super().__init__(self.browser, self.context)
