from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    TITLE_NEW = (By.CSS_SELECTOR,"h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")

class AlertsPageLocators:

    BUTTON_TO_SEE_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    BUTTON_ALERT_AFTER_5_SEC = (By.CSS_SELECTOR, "button[id='timerAlertButton']")

    BUTTON_ALERT_CONFORM_BOX = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")

    BUTTON_ALERT_PROMPT_BOX = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")

class FramesPageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id=frame1]")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id=frame2]")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class NestedFramesLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")
