from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def get_survey_numbers(district, mandal, village):
    url = 'https://dharani.telangana.gov.in/knowLandStatus'

    driver = webdriver.Chrome()

    driver.get(url)

    section = driver.find_element(By.TAG_NAME, 'section')

    selections = section.find_elements(By.TAG_NAME, 'select')

    district_id = selections[0]
    mandal_id = selections[1]
    village_id = selections[2]
    survey_id = selections[3]

    time.sleep(5)

    district_options = district_id.find_elements(By.TAG_NAME, 'option')
    options_list = [option for option in district_options]

    for option in options_list[1:]:
        if district in option.text:
            option.click()
            break
    else:
        print('no match')

    time.sleep(10)

    mandal_options = mandal_id.find_elements(By.TAG_NAME, 'option')
    options_list = [option for option in mandal_options]

    for option in options_list[1:]:
        if mandal in option.text:
            option.click()
            break
    else:
        print('no match')

    time.sleep(10)

    village_options = village_id.find_elements(By.TAG_NAME, 'option')
    options_list = [option for option in village_options]

    for option in options_list[1:]:
        if village in option.text:
            option.click()
            break
    else:
        print('no match')

    time.sleep(10)

    survey_options = survey_id.find_elements(By.TAG_NAME, 'option')
    survey_numbers = [option.text for option in survey_options]


    driver.quit()

    return survey_numbers[1:]


print(get_survey_numbers("Adilabad", "Bela", "Bela"))





