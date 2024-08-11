from features.modules.ui.page_objects.base_page import BasePage
from features.modules.ui.page_objects.browser_content import *
from features.modules.ui.page_objects.base_page import *

class ProductsPage(BasePage):
  def __init__(self, browser, context):
   
    self.browser = browser
    self.context = context

    self.products_title        = self.browser.element(class_name="collections__heading", text="Products")
    self.products_list_parent  = self.browser.element(class_name="collections__product-cards")
    self.products_list         = self.products_list_parent.element(class_name="products__list")

    self.search_box            = self.browser.element(type="search")


    super().__init__(self.browser, self.context)

  def is_course_visible(self, course_name):
    self.course = self.browser.element(class_name="card__name", text=course_name)
    
    try:
        self.course.wait_until(method=lambda e: e.present, timeout=10)
        return self.course.visible
    except Exception as e:
        print(f"Failed to find or wait for visibility of course '{course_name}': {e}")
        return False

