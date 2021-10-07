import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/Users/jcord/PycharmProjects/designHouse"


class Driver:

    def initializeWebDriver(self, browser):
        if browser.lower() == "gc":
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(8)
        elif browser == "ff":
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(8)
        else:
            print("wrong browser name")

    def fullScreenBrowser(self):
        self.driver.maximize_window()

    def navigateToWebPage(self, url):
        self.driver.get(url)

    def closeCurrentBrowser(self):
        self.driver.close()

    def quitCurrentBrowsers(self):
        self.driver.quit()

    def pageShouldContainElement(self, elementSelector):
        selectorParts = elementSelector.split("=")
        typeSelector = selectorParts[0]
        selector = selectorParts[1]
        try:
            if typeSelector == "css":
                self.driver.find_element_by_css_selector(selector)
            if typeSelector == "name":
                self.driver.find_element_by_name(selector)
                print()
        except Exception:
            return False
        return True

    def clickElement(self, elementSelector):
        selectorParts = elementSelector.split("=")
        typeSelector = selectorParts[0]
        selector = selectorParts[1]
        if typeSelector == "css":
            element = self.driver.find_element_by_css_selector(selector)
            element.click()

        elif typeSelector == "name":
            element = self.driver.find_element_by_name(selector)
            element.click()
        elif typeSelector == "class":
            element = self.driver.find_element_by_class_name(selector)
            element.click()

    def waitUntilElementIsVisible(self, elementSelector):
        selectorParts = elementSelector.split("=")
        typeSelector = selectorParts[0]
        selector = selectorParts[1]
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def sendtextToElement(self, elementSelector, text):
        selectorParts = elementSelector.split("=")
        typeSelector = selectorParts[0]
        selector = selectorParts[1]
        if typeSelector == "css":
            element = self.driver.find_element_by_css_selector(selector)
            element.send_keys(text)
        elif typeSelector == "name":
            element = self.driver.find_element_by_name(selector)
            element.send_keys(text)

    def elementIsDisplayed(self, elementSelector):
        selectorParts = elementSelector.split("=")
        typeSelector = selectorParts[0]
        selector = selectorParts[1]
        if typeSelector == "css":
            element = self.driver.find_element_by_css_selector(selector)
            displayed = element.is_displayed()
        elif typeSelector == "name":
            element = self.driver.find_element_by_name(selector)
            displayed = element.is_displayed()
        return displayed

    def getElementText(self, elementSelector):
        selectorParts = elementSelector.split("=")
        typeSelector = selectorParts[0]
        selector = selectorParts[1]
        if typeSelector == "css":
            element = self.driver.find_element_by_css_selector(selector)
            text = element.text

        elif typeSelector == "name":
            element = self.driver.find_element_by_name(selector)
            text = element.text
        return text

    def getPageURL(self):
        currentURL = self.driver.current_url
        return currentURL


searchBar = """css=#search > input"""
searchButton = """css=#search > span > button"""
myAccountMenu = """css=#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md"""
myAccountMenuOpen = """css=#top-links > ul > li.dropdown.open"""
myAccountSubmenuRegister = """css=#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a"""
myAccountSubmenuLogin = """css=#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a"""
aboutUsLink = """css=body > footer > div > div > div:nth-child(1) > ul > li:nth-child(1) > a"""
shoppingCartButton = """css=#cart > button"""
emptyCartMessage = """css=#cart > ul > li > p"""
shoppingCartAmountButton = """css=#cart-total"""
productInList = """css=#content > div.row > div:nth-child(1)"""


'''driver = Driver()
driver.initializeWebDriver("gc")
driver.navigateToWebPage("http://opencart.abstracta.us/")
driver.clickElement(productInList)
#driver.closeCurrentBrowser()'''







