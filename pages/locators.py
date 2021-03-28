from selenium.webdriver.common.by import By


class MainPageLocators:
    ADD_FILES = (By.CSS_SELECTOR, "#file-btn")
    EMAIL = (By.CSS_SELECTOR, "#email")
    CONTINUE = (By.CSS_SELECTOR, "button.h3d-button.h3d-button--primary.u-margin-top-1.u-flex-1")


class QuoteOverviewPageLocators:
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.h3d-actions__total-price")
    CROSS_BUTTON = By.CLASS_NAME, "h3d-button.new-feature-walkthrough-dialog__close-button"


class ErrorPanelLocators:
    ERROR = (By.CSS_SELECTOR, ".h3d-notification-inline.h3d-notification-inline--size_l.h3d-notification-inline--level_error")
