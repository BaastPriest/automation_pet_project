import random
from selenium.webdriver.common.by import By


class FormsPageLocators:

    FIRST_NAME_LOCATOR = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_LOCATOR = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_LOCATOR = (By.CSS_SELECTOR, 'input[id="userEmail"]')

    GENDER_LOCATOR = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1,3)}"]')

    MOBILE_NUMBER_LOCATOR = (By.CSS_SELECTOR, 'input[id="userNumber"]')

    DATE_OF_BIRTH_LOCATOR = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')

    SUBJECTS_LABEL_LOCATOR = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')

    HOBBIES_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1,3)}"]')

    UPLOAD_PICTURE_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    CURRENT_ADDRESS_LOCATOR = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')

    STATE_SELECT_LOCATOR = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')

    CITY_SELECT_LOCATOR = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table responsive
    TABLE_RESPONSIVE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')


