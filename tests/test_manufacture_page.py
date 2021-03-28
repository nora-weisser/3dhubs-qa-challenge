import os

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import MainPageLocators, QuoteOverviewPageLocators
from pages.manufacture_page import ManufacturePage

BASE_DIR = os.path.dirname(os.path.abspath('../resources/STEP_format_file.STEP'))

STEP_FORMAT_FILE_PATH = os.path.join(BASE_DIR, 'STEP_format_file.STEP')
DM_FORMAT_FILE_PATH = os.path.join(BASE_DIR, '3DM_format_file.3dm')
IGS_FORMAT_FILE_PATH = os.path.join(BASE_DIR, 'IGS_format_file.IGS')
SAT_FORMAT_FILE_PATH = os.path.join(BASE_DIR, 'SAT_format_file.SAT')
SLDPRT_FORMAT_FILE_PATH = os.path.join(BASE_DIR, 'SLDPRT_format_file.SLDPRT')
STP_FORMAT_FILE_PATH = os.path.join(BASE_DIR, 'STP_format_file.stp')
X_T_FORMAT_FILE_PATH = os.path.join(BASE_DIR, 'x_t_format_file.x_t')

ASSEMBLY_FILE_PATH = os.path.join(BASE_DIR, 'ASSEMBLY_file.stp')

MANUFACTURE_PAGE_LINK = 'https://www.3dhubs.com/manufacture/'

DEFAULT_TIMEOUT = 30

EMAIL = "eleo.belova@yandex.ru"

"""
This test is checking model uploading on https://www.3dhubs.com/manufacture/
Check all acceptable file formats: .3dm, .stp, .IGS, .SAT, .SLADPRT, .STEP, .x_t.
All files are located in the resources folder.

Steps to reproduce:
1. Open https://www.3dhubs.com/manufacture/
2. Upload file

Expected result: pricing quote should appear
"""


@pytest.mark.parametrize('PATH', [STEP_FORMAT_FILE_PATH, DM_FORMAT_FILE_PATH, IGS_FORMAT_FILE_PATH,
                                  SAT_FORMAT_FILE_PATH, SLDPRT_FORMAT_FILE_PATH, STP_FORMAT_FILE_PATH,
                                  X_T_FORMAT_FILE_PATH])
def test_customer_can_add_design_step_format(browser, PATH):
    # given
    link = MANUFACTURE_PAGE_LINK
    page = ManufacturePage(browser, link)
    page.open()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(EC.presence_of_element_located(MainPageLocators.ADD_FILES))

    # when
    page.add_design(browser, PATH, EMAIL)
    button = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(QuoteOverviewPageLocators.CROSS_BUTTON))
    button.click()

    # then
    page.should_be_pricing_quote()
    page.should_not_be_error_panel()


"""
This test is checking complex model (assembly) uploading on https://www.3dhubs.com/manufacture/

Steps to reproduce:
1. Open https://www.3dhubs.com/manufacture/
2. Upload file

Expected result: error message should be shown
"""


def test_customer_adds_assembly_with_error(browser):
    # given
    link = MANUFACTURE_PAGE_LINK
    page = ManufacturePage(browser, link)
    page.open()
    WebDriverWait(browser, DEFAULT_TIMEOUT).until(EC.presence_of_element_located(MainPageLocators.ADD_FILES))

    # when
    page.add_assembly_with_error(browser, ASSEMBLY_FILE_PATH, EMAIL)
    button = WebDriverWait(browser, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(QuoteOverviewPageLocators.CROSS_BUTTON))
    button.click()

    # then
    page.should_be_error_panel()
