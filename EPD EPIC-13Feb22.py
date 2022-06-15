from selenium import webdriver
from pprint import pprint as pp
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time


# Simple ---------------------------------------------------------------------------------------------------------------
def click_radios(driver, display_dict):
    content = driver_content(driver, xpath_content)
    strXpath = r"//div[@class='custom-radio custom-radio--inline']"
    elems = find_elements(display_dict, content, "xpath", strXpath, '1', verbose=False)
    elems[0].click()
    elems[3].click()


def click_select(driver, display_dict):
    content = driver_content(driver, xpath_content)
    strXpath = r"//div[@class='btn btn--orange submit-btn']"
    select_btn = find_elements(display_dict, content, "xpath", strXpath, '4', verbose=False)
    select_btn[0].click()
# Simple ---------------------------------------------------------------------------------------------------------------


# Dropdown -------------------------------------------------------------------------------------------------------------
def click_dropbox_elem(driver, display_dict, xpath_dropbox, xpath_elem):
    content = driver_content(driver, xpath_content)
    dropbox = find_elements(display_dict, content, "xpath", xpath_dropbox, '2', verbose=False)
    dropbox[0].click()

    strXpath = r"//ul[@class='custom-select__list scrollable default-skin']"
    dropbox_hidden = find_elements(display_dict, content, "xpath", strXpath, '3-1', verbose=False)
    selected = find_elements(display_dict, dropbox_hidden[0], "xpath", xpath_elem, '3-2', verbose=False)
    selected = selected[0]
    action.move_to_element(selected).click(selected).perform()
# Dropdown -------------------------------------------------------------------------------------------------------------


# Options --------------------------------------------------------------------------------------------------------------
def find_option_elem_list(driver, display_dict, xpath):
    content = driver_content(driver, xpath_content)
    option_list = find_elements(display_dict, content, "xpath", xpath, '5-1', verbose=False)
    option = option_list[0]
    strXpath = r".//option"
    selected_option = find_elements(display_dict, option, "xpath", strXpath, '5-2', verbose=False)
    return selected_option


def click_all_options(driver, display_dict, xpath):
    options = find_option_elem_list(driver, display_dict, xpath)
    num = len(options)
    for _ in range(num):
        options = find_option_elem_list(driver, display_dict, xpath)
        option = [e for e in options if e.text != ''][0]
        action.double_click(option).perform()
# Options --------------------------------------------------------------------------------------------------------------


# Util -----------------------------------------------------------------------------------------------------------------
def driver_content(driver, xpath_content):
    return driver.find_element("xpath", xpath_content)


def find_element(display, main, type, name, custom, verbose=True):
    elem = main.find_element(type, name)
    save_elem_attr(display, elem, name, custom, verbose)
    return elem


def find_elements(display, main, type, name, custom, verbose=True):
    elems = main.find_elements(type, name)
    for idx, e in enumerate(elems):
        save_elem_attr(display, e, name, f'{custom}@{idx + 1}', verbose)
    return elems


def save_elem_attr(display, element, name, custom, verbose=True):
    if verbose:
        # display[(custom, name, 'accessible name')] = element.accessible_name
        # display[(custom, name, 'id')] = element.id
        # display[(custom, name, 'tag_name')] = element.tag_name
        display[(custom, name, 'text')] = element.text
        # display[(custom, name, 'enabled')] = element.is_enabled()
        # display[(custom, name, 'selected')] = element.is_selected()
        # display[(custom, name, 'displayed')] = element.is_displayed()
# Util -----------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    try:
        zone_list = ["Deep Bay", "Eastern Buffer", "Junk Bay", "Mirs Bay", "North Western", "Port Shelter",
                     "Southern", "Tolo Harbour and Channel", "Victoria Harbour", "Western Buffer"]
        start_year = '2000'

        dictDisplay = dict()
        driver = webdriver.Chrome()
        # create action chain object
        action = ActionChains(driver)

        xpath_content = "//main[@id='content']"

        for loco in zone_list[0:1]:
            driver.get("https://cd.epic.epd.gov.hk/EPICRIVER/marine/download/")
            print(loco)

            # 1
            click_radios(driver, dictDisplay)
            # 2
            strXpath_drop = r"//a[@class='custom-select__trigger'][@aria-labelledby='form:wzterControlZone_label']"
            strXpath_elem = rf".//li[@data-val='{loco}']"
            click_dropbox_elem(driver, dictDisplay, strXpath_drop, strXpath_elem)
            # 3
            click_select(driver, dictDisplay)
            # 4
            strXpath_drop = r"//a[@class='custom-select__trigger'][@aria-labelledby='form:FromYear_label']"
            strXpath_elem = rf".//li[@data-val='{start_year}']"
            click_dropbox_elem(driver, dictDisplay, strXpath_drop, strXpath_elem)
            # 5
            xpath = r"//select[@name='unselectStation']"
            click_all_options(driver, dictDisplay, xpath)
            # 6
            xpath = r"//select[@name='unselectParameter']"
            click_all_options(driver, dictDisplay, xpath)
            # 7
            click_select(driver, dictDisplay)
    # except:
    #     print('error')
    #     pass
    finally:
        # pp(dictDisplay)
        # time.sleep(10)
        driver.close()
