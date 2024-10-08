from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # fields form
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS =(By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:

    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "//input[@id='noRadio' and @disabled]")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablesPageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT =(By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = (".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # update info about person
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:

    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")  # 'div[class="mt-4"]:nth-child(3n)'

    # result
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_ME_BUTTON_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:

    # Following links will open new tab
    HOME_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    # Following links will send an api call
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")


class FilePageLocators:
    # upload
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_FILE_MSG = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    # download
    DOWNLOAD_FILE_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")


class DynamicPropertiesPageLocators:
    ENABLE_5_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id = 'enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_5_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")
