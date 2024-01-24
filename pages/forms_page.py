import os
from selenium.webdriver import Keys

from generator.generator import generated_person, convert_phone_number_live_only_numbers, \
    select_one_random_photo_of_a_cat, select_random_subjects
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name = select_one_random_photo_of_a_cat()
        self.remove_footer()
        formatted_phone_num = convert_phone_number_live_only_numbers(person.mobile)
        self.element_is_visible(self.locators.FIRST_NAME_LOCATOR).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_LOCATOR).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_LOCATOR).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_LOCATOR).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER_LOCATOR).send_keys(formatted_phone_num)
        self.element_is_visible(self.locators.SUBJECTS_LABEL_LOCATOR).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECTS_LABEL_LOCATOR).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX_LOCATOR).click()
        self.element_is_present(self.locators.UPLOAD_PICTURE_BUTTON_LOCATOR).send_keys(file_name)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_LOCATOR).send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.STATE_SELECT_LOCATOR))
        self.element_is_visible(self.locators.STATE_SELECT_LOCATOR).click()
        self.element_is_visible(self.locators.STATE_INPUT_LOCATOR).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY_SELECT_LOCATOR).click()
        self.element_is_visible(self.locators.CITY_INPUT_LOCATOR).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON_LOCATOR).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.TABLE_RESPONSIVE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data

    def upload_photo(self):
        file_name = select_one_random_photo_of_a_cat()
        self.element_is_present(self.locators.UPLOAD_PICTURE_BUTTON_LOCATOR).send_keys(file_name)

    def fill_form_fields_with_random_value(self):
        person = next(generated_person())
        file_name = select_one_random_photo_of_a_cat()
        self.remove_footer()
        formatted_phone_num = convert_phone_number_live_only_numbers(person.mobile)
        self.element_is_visible(self.locators.FIRST_NAME_LOCATOR).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_LOCATOR).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_LOCATOR).send_keys(person.email)
        #TODO DATE OF BIRTH
        self.element_is_visible(self.locators.GENDER_LOCATOR).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER_LOCATOR).send_keys(formatted_phone_num)
        self.element_is_visible(self.locators.SUBJECTS_LABEL_LOCATOR).send_keys(select_random_subjects())  # TODO
        self.element_is_visible(self.locators.SUBJECTS_LABEL_LOCATOR).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX_LOCATOR).click()
        self.element_is_present(self.locators.UPLOAD_PICTURE_BUTTON_LOCATOR).send_keys(file_name)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_LOCATOR).send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.STATE_SELECT_LOCATOR))
        self.element_is_visible(self.locators.STATE_SELECT_LOCATOR).click()
        self.element_is_visible(self.locators.STATE_INPUT_LOCATOR).send_keys(Keys.RETURN)  # TODO
        self.element_is_visible(self.locators.CITY_SELECT_LOCATOR).click()
        self.element_is_visible(self.locators.CITY_INPUT_LOCATOR).send_keys(Keys.RETURN)  # TODO
        self.element_is_visible(self.locators.SUBMIT_BUTTON_LOCATOR).click()
        return person