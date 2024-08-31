Feature: UI

	@ui
	Scenario: UI: The user can add one product to the cart
    Given UI - Main: The user is on the home page
    When UI - Main: The user goes to the category "Gear" products page
    Then UI - Main: The page "Gear" is opened
    When UI - Main: The user goes to the sub-category "Bags" products page
    Then UI - Main: The page "Bags" is opened
    When UI - Product: The user add the product "Push It Messenger Bag" to the cart
    Then UI - Cart: The cart icon is updated and contains "1" products
    When UI - Cart: The user goes to cart
    Then UI - Main: The page "Shopping Cart" is opened
    Then UI - Cart: Check the product "Push It Messenger Bag" is visible on the cart