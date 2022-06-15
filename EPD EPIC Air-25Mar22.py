from selenium import webdriver
from pprint import pprint as pp
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    try:
        start_year = 1990
        end_year = 2020
        lst_yr = [*map(str, range(start_year, end_year + 1))]

        driver = webdriver.Chrome()
        driver.get("https://cd.epic.epd.gov.hk/EPICDI/air/yearly/")

        xpath_content = "//main[@id='content']"
        content = driver.find_element(By.XPATH, xpath_content)

        lst_elems = content.find_elements(By.CSS_SELECTOR, 'a')
        lst_id = [e for e in lst_elems if e.text in lst_yr]

        for e in lst_id:
            print(e.accessible_name, e.text)
            e.click()

    finally:
        driver.close()
