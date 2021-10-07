from behave import *
from Driver import Driver

searchBar = """css=#search > input"""
searchButton = """css=#search > span > button"""
myAccountMenu = """css=#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md"""
myAccountMenuOpen = """css=#top-links > ul > li.dropdown.open"""
myAccountSubmenuRegister = """css=#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a"""
myAccountSubmenuLogin = """css=#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a"""
aboutUsLink = """css=body > footer > div > div > div:nth-child(1) > ul > li:nth-child(1) > a"""
shoppingCartButton = """css=#cart > button"""
shoppingCartAmountButton = """css=#cart-total"""
emptyCartMessage = """css=#cart > ul > li > p"""
productInList = """css=#content > div.row > div:nth-child(1)"""
driver = Driver()


@given('The test user has loaded the Your Store web page')
def step_impl(context):
    driver.initializeWebDriver("gc")
    driver.fullScreenBrowser()
    driver.navigateToWebPage("http://opencart.abstracta.us/")


@given('The "My Account" dropdown menu is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(myAccountMenu)
    assert True == exist


@when('The test user clicks the "My Account" button')
def step_impl(context):
    driver.clickElement(myAccountMenu)


@then('The dropdown menu is open')
def step_impl(context):
    exist = driver.pageShouldContainElement(myAccountMenuOpen)
    assert True == exist


@then('The "Register" dropdown item  is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(myAccountSubmenuRegister)
    assert True == exist


@then('The "Login" dropdown item is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(myAccountSubmenuLogin)
    assert True == exist
    driver.closeCurrentBrowser()


@given('The search bar is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(searchBar)
    assert True == exist

    displayed = driver.elementIsDisplayed(searchBar)
    assert True == displayed


@given('The test user inputs a valid string in the search bar')
def step_impl(context):
    driver.sendtextToElement(searchBar, "Mac")


@when('The user clicks the search button')
def step_impl(context):
    driver.clickElement(searchButton)


@then('The test user is redirected to the search results page')
def step_impl(context):
    currentURL = driver.getPageURL()
    valid = currentURL == "http://opencart.abstracta.us/index.php?route=product/search&search=Mac"
    assert True == valid
    driver.closeCurrentBrowser()


@given('The "shopping cart" button is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(shoppingCartButton)
    assert True == exist

    displayed = driver.elementIsDisplayed(shoppingCartButton)
    assert True == displayed


@given('The shopping cart is empty')
def step_impl(context):
    text = driver.getElementText(shoppingCartAmountButton)
    textArray = text.split(" ")
    amountItems = textArray[0]
    empty = amountItems == "0"
    assert True == empty


@when('The test user clicks the "shopping cart" button')
def step_impl(context):
    driver.clickElement(shoppingCartButton)


@then('The "Your shopping cart is empty!" message is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(emptyCartMessage)
    assert True == exist

    displayed = driver.elementIsDisplayed(emptyCartMessage)
    assert True == displayed
    driver.closeCurrentBrowser()


@given('The featured list is displaying at least one product')
def step_impl(context):
    exist = driver.pageShouldContainElement(productInList)
    assert True == exist

    displayed = driver.elementIsDisplayed(productInList)
    assert True == displayed


@when('The test user clicks a product from the list')
def step_impl(context):
    driver.clickElement(productInList)


@then('The test user is redirected to the product page')
def step_impl(context):
    currentURL = driver.getPageURL()
    valid = currentURL == "http://opencart.abstracta.us/index.php?route=product/product&product_id=43"
    assert True == valid
    driver.closeCurrentBrowser()


@given('The "About Us" link is displayed')
def step_impl(context):
    exist = driver.pageShouldContainElement(aboutUsLink)
    assert True == exist

    displayed = driver.elementIsDisplayed(aboutUsLink)
    assert True == displayed


@when('The test user clicks the "About Us" link')
def step_impl(context):
    driver.clickElement(aboutUsLink)


@then('The test user is redirected to the About Us page')
def step_impl(context):
    currentURL = driver.getPageURL()
    valid = currentURL == "http://opencart.abstracta.us/index.php?route=information/information&information_id=4"
    assert True == valid
    driver.closeCurrentBrowser()