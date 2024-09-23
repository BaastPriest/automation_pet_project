import os
import random, allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, FilePage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name,email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, f"expected {full_name} but was {output_name}"
            assert email == output_email, f"expected {email} but was {output_email}"
            assert current_address.replace("\n", " ") == output_current_address.replace("\n", " "), f"expected {current_address} but was {output_current_address}"
            assert permanent_address.replace("\n", " ") == output_permanent_address.replace("\n", " "), f"expected {permanent_address} but was {output_permanent_address}"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, f'Expected selected checkboxes {input_checkbox} but actual {output_result}'

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check RadioButton")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_the_radio_button('Yes')
            output_yes = radio_button_page.get_output_result_radio_button()
            radio_button_page.click_the_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result_radio_button()
            assert output_yes == 'Yes', f'Expected selected radio button "Yes", but actual {output_yes}'
            assert output_impressive == 'Impressive', f'Expected selected radio button "Impressive", but actual {output_impressive}'

        @allure.title("Check disabled RadioButton")
        def test_disabled_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            disabled_radio_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='noRadio' and @disabled]")))
            assert disabled_radio_button.get_attribute(
                'disabled') == 'true', 'Radio button should be disabled, but it is not.'
            assert not disabled_radio_button.is_selected(), 'Disabled radio button should not be selectable.'
            driver.execute_script("arguments[0].click();", disabled_radio_button)
            assert not disabled_radio_button.is_selected(), 'Disabled radio button should not change its state after a click.'

    @allure.feature("WebTables")
    class TestWebTables:
        @allure.title("Check to add a person to the table")
        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            table_result = web_tables_page.check_new_person()
            assert new_person == [x.strip() for x in table_result]

        @allure.title("Check to search a person in the table")
        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[random.randint(0,5)]
            web_tables_page.search_a_person(key_word)
            table_result = web_tables_page.check_searched_person()
            assert key_word in table_result, f'The person with key word {key_word}, did not find in table result {table_result}'

        @allure.title("Check update person info in the table")
        def test_web_table_update_person_info(self, driver): #TODO make the test change different parameters
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_a_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_searched_person()
            assert age in row, f'The person card has not been changed'

        @allure.title("Check delete person from the table")
        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_new_person()[3]
            web_tables_page.search_a_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()
            assert text == "No rows found"

        @allure.title("Check change count row in table")
        def test_web_table_change_count_row(self, driver): #with BUG
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 50, 50, 100], "Number of rows in the table has not been changend or has not been changed incorrectly"

    @allure.feature("ButtonPage")
    class TestButtonPage:
        @allure.title("Check click on buttons")
        def test_different_click_on_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have done a double click", "The double click button was not clicked"
            assert right == "You have done a right click", "The right click button was not clicked"
            assert click == "You have done a dynamic click", "The dynamic click button was not clicked"

    @allure.feature("LinksPage")
    class TestLinksPage:
        @allure.title("Check link")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_home_link()
            assert href_link == current_url, "The link is broken os url is incorrect"

        @allure.title("Check broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400, "The link works or the status code is not 400"

    @allure.feature("FilePage")
    class TestFilePage:
        @allure.title("Check upload file")
        def test_upload_file(self, driver):
            upload_page = FilePage(driver, "https://demoqa.com/upload-download")
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert os.path.basename(file_name) == result, "The file has not been uploaded"

        @allure.title("Check download file")
        def test_download_file(self, driver):
            download_page = FilePage(driver, "https://demoqa.com/upload-download")
            download_page.open()
            check = download_page.download_file()
            assert check is True, "The file has not been downloaded"

    @allure.feature("DynamicProperties")
    class TestDynamicProperties:
        @allure.title("Check button enable 5 sec")
        def test_enable_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            enable_button = dynamic_properties_page.check_enable_button()
            assert enable_button is True, "Button did not enable after 5 second"

        @allure.title("Check button visible after 5 sec")
        def test_visible_after_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, "Button did not appear after 5 second"

        @allure.title("Check button change color")
        def test_change_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_color()
            assert color_before != color_after, "Color did not change"
