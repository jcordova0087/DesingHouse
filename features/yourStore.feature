Feature: Your store page behaviors

    Scenario: The test user clicks the My account dropdown menu in the top menu
      Given The test user has loaded the Your Store web page
      And The "My Account" dropdown menu is displayed
      When The test user clicks the "My Account" button
      Then The dropdown menu is open
      And The "Register" dropdown item  is displayed
      And The "Login" dropdown item is displayed


    Scenario: The test user performs a search in the search bar
      Given The test user has loaded the Your Store web page
      And The search bar is displayed
      And The test user inputs a valid string in the search bar
      When The user clicks the search button
      Then The test user is redirected to the search results page


    Scenario: The test user clicks the shopping cart button when is empty
      Given The test user has loaded the Your Store web page
      And The "shopping cart" button is displayed
      And The shopping cart is empty
      When The test user clicks the "shopping cart" button
      Then The "Your shopping cart is empty!" message is displayed


    Scenario: The test user clicks an item from the featured list
      Given The test user has loaded the Your Store web page
      And The featured list is displaying at least one product
      When The test user clicks a product from the list
      Then The test user is redirected to the product page


    Scenario: The test user clicks the About Us link
      Given The test user has loaded the Your Store web page
      And The "About Us" link is displayed
      When The test user clicks the "About Us" link
      Then The test user is redirected to the About Us page





