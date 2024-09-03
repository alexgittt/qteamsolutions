Feature: UI - Main

	@ui @main
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

    @ui @main
	Scenario: UI: The user can add three products to the cart
    Given UI - Main: The user is on the home page
    When UI - Main: The user goes to the category "Gear" products page
    Then UI - Main: The page "Gear" is opened
    When UI - Main: The user goes to the sub-category "Bags" products page
    Then UI - Main: The page "Bags" is opened
    When UI - Product: The user add the product "Push It Messenger Bag" to the cart
    Then UI - Cart: The cart icon is updated and contains "1" products
    When UI - Product: The user add the product "Overnight Duffle" to the cart
    Then UI - Cart: The cart icon is updated and contains "2" products
    When UI - Product: The user add the product "Driven Backpack" to the cart
    Then UI - Cart: The cart icon is updated and contains "3" products
    When UI - Cart: The user goes to cart
    Then UI - Main: The page "Shopping Cart" is opened
    Then UI - Cart: Check the product "Push It Messenger Bag" is visible on the cart
    Then UI - Cart: Check the product "Overnight Duffle" is visible on the cart
    Then UI - Cart: Check the product "Driven Backpack" is visible on the cart
   
    @ui @main
	Scenario: UI: The user can add one product to the cart and finalize the order
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
    When UI - Cart: The user proceed to checkout
    Then UI - Main: The shipping address page is displayed
    When UI - Main: The user fill the shipping address with the address "first_buyer"
    Then UI - Main: The payment screen is displayed
    When UI - Main: The user place order
    Then UI - Main: The order is successfully placed

    @ui @main
	Scenario: UI: The user can add more products to the cart and finalize the order
    Given UI - Main: The user is on the home page
    When UI - Main: The user goes to the category "Gear" products page
    Then UI - Main: The page "Gear" is opened
    When UI - Main: The user goes to the sub-category "Bags" products page
    Then UI - Main: The page "Bags" is opened
    When UI - Product: The user add the product "Push It Messenger Bag" to the cart
    Then UI - Cart: The cart icon is updated and contains "1" products
    When UI - Product: The user add the product "Overnight Duffle" to the cart
    Then UI - Cart: The cart icon is updated and contains "2" products
    When UI - Cart: The user goes to cart
    Then UI - Main: The page "Shopping Cart" is opened
    Then UI - Cart: Check the product "Push It Messenger Bag" is visible on the cart
    When UI - Cart: The user proceed to checkout
    Then UI - Main: The shipping address page is displayed
    When UI - Main: The user fill the shipping address with the address "first_buyer"
    Then UI - Main: The payment screen is displayed
    When UI - Main: The user place order
    Then UI - Main: The order is successfully placed

    @ui @main
	Scenario: UI: The user can add one product to the cart and finalize the order
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
    When UI - Cart: The user proceed to checkout
    Then UI - Main: The shipping address page is displayed
    When UI - Main: The user fill the shipping address with the address "buyer_with_empty_field"
    Then UI - Main: Field error message is displayed
