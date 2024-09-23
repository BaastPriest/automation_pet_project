import base64
import os
import random
import time
import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from generator import generator
from generator.generator import generated_person, generate_text_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators, FilePageLocators, DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step("Fill full name, email, address"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("Click Submit btn"):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Check filled form")
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("Open full list")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("Click random checkbox")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    @allure.step("Get checked checkboxes")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(" ", "").replace("doc", "").replace(".", "").lower()

    @allure.step("Get output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Click the radio button")
    def click_the_radio_button(self, choice):
        choices = {'Yes': self.locators.YES_RADIO_BUTTON,
                   'Impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
                   'No': self.locators.NO_RADIO_BUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step("Get output result of radio button")
    def get_output_result_radio_button(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    @allure.step("Add new person")
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_clickable(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
            count -= 1
        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step("Check new person")
    def check_new_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step("Search a person")
    def search_a_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step("Check searched person")
    def check_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step("Update person info")
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step("Delete person")
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step("Check deleted rows")
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step("Select up to some rows")
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 50, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value={x}]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step("Check count rows")
    def check_count_rows(self):
        list_rows = self.element_is_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("Click on different button")
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_the_button(self.locators.DOUBLE_CLICK_MESSAGE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_the_button(self.locators.RIGHT_CLICK_MESSAGE)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_the_button(self.locators.CLICK_ME_BUTTON_MESSAGE)

    @allure.step("Check clicked the button")
    def check_clicked_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step("Check new tab home link")
    def check_new_tab_home_link(self):  # TODO create tests for all links
        home_link = self.element_is_visible(self.locators.HOME_LINK)
        link_href = home_link.get_attribute("href")
        request = requests.get(link_href)
        if request.status_code == 200:
            home_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code  # TODO use Try Except

    @allure.step("Check broken link")
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code


class FilePage(BasePage):
    locators = FilePageLocators()

    @allure.step("Upload file")
    def upload_file(self):
        file_name, path = generate_text_file("txt")
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE_MSG).text
        return file_name.split("\\")[-1], text.split("\\")[-1]

    @allure.step("Download file")
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE_BUTTON).get_attribute("href")
        link_temp = base64.b64decode(link)
        path_file_name = generator.generate_file_name("jpg")
        with open(path_file_name, 'wb+') as f:
            offset = link_temp.find(b'\xff\xd8')
            f.write(link_temp[offset:])
            check_file = os.path.exists(path_file_name)
            f.close()
        os.remove(path_file_name)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step("Check enable button")
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_5_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step("Check changed color button")
    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(5)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after

    @allure.step("Check appear button")
    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True
