Feature: UI - Cart

 @ui @cart
	Scenario: UI: The user can see a message when the cart is empty
    Given UI - Main: The user is on the home page
    When UI - Cart: The user goes to the empty cart
    Then UI - Cart: Empty message is displayed

@ui @cart
	Scenario: UI: The user can delete product from the cart
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
    When UI - Cart: The user delete the product from the cart
    Then UI - Cart: The shopping cart main page is empty

@ui @cart
	Scenario: UI: The user can update the quantity in the cart
    Given UI - Main: The user is on the home page
    When UI - Main: The user goes to the category "Gear" products page
    Then UI - Main: The page "Gear" is opened
    When UI - Main: The user goes to the sub-category "Bags" products page
    Then UI - Main: The page "Bags" is opened
    When UI - Product: The user add the product "Push It Messenger Bag" to the cart
    Then UI - Cart: The cart icon is updated and contains "1" products
    When UI - Cart: The user goes to cart
    Then UI - Main: The page "Shopping Cart" is opened
    When UI - Cart: The user update the quantity of the product to "5"
    Then UI - Cart: The quantity is "5"
