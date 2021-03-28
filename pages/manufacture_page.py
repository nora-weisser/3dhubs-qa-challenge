from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import MainPageLocators, ErrorPanelLocators, QuoteOverviewPageLocators
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 10


class ManufacturePage(BasePage):
    def add_assembly_with_error(self, browser, element_abspath, email):
        button_add_files = self.browser.find_element(*MainPageLocators.ADD_FILES)
        button_add_files.send_keys(element_abspath)
        email_folder = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.EMAIL))
        email_folder.send_keys(email)
        browser.find_element(*MainPageLocators.CONTINUE).click()

    def add_design(self, browser, element_abspath, email):
        button_add_files = self.browser.find_element(*MainPageLocators.ADD_FILES)
        button_add_files.send_keys(element_abspath)
        email_folder = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.EMAIL))
        email_folder.send_keys(email)
        browser.find_element(*MainPageLocators.CONTINUE).click()

    def should_be_error_panel(self):
        assert self.is_element_present(*ErrorPanelLocators.ERROR), "Error panel should be on the page"

    def should_not_be_error_panel(self):
        assert self.is_not_element_present(*ErrorPanelLocators.ERROR), "Error panel is on the page, but shouldn't be"

    def should_be_pricing_quote(self):
        assert self.browser.find_element(
            *QuoteOverviewPageLocators.TOTAL_PRICE).text, 'There is no pricing quote on the page'
