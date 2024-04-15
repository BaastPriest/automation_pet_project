import random
import time

from selenium.common import UnexpectedAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self): #TODO add to base_page
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self): #TODO serch tab / window. One def: check_opened_new_tab + check_opened_new_window
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.BUTTON_TO_SEE_ALERT).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self): # TODO add count of sec
        self.element_is_visible(self.locators.BUTTON_ALERT_AFTER_5_SEC).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.BUTTON_ALERT_CONFORM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f"autotest{random.randint(0,999)}"
        self.element_is_visible(self.locators.BUTTON_ALERT_PROMPT_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result