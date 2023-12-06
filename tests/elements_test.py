import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name,email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, f"expected {full_name} but was {output_name}"
            assert email == output_email, f"expected {email} but was {output_email}"
            assert current_address == output_current_address, f"expected {current_address} but was {output_current_address}"
            assert permanent_address == output_permanent_address, f"expected {permanent_address} but was {output_permanent_address}"


    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_rezult()
            assert input_checkbox == output_result, f'Expected selected checkboxes {input_checkbox} but actual {output_result}'


    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_the_radio_button('Yes')
            output_yes = radio_button_page.get_output_rezult_radio_button()
            radio_button_page.click_the_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_rezult_radio_button()
            radio_button_page.click_the_radio_button('No')
            output_no = radio_button_page.get_output_rezult_radio_button()

            assert output_yes == 'Yes', f'Expected selected radio button "Yes", but actual {output_yes}'
            assert output_impressive == 'Impressive', f'Expected selected radio button "Impressive", but actual {output_impressive}'
            assert output_no == 'No', f'Expected selected radio button "No", but actual {output_no}'

    class TestWebTables:

        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            table_result = web_tables_page.check_new_person()
            assert new_person in table_result


        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[random.randint(0,5)]
            web_tables_page.search_a_person(key_word)
            table_result = web_tables_page.check_searched_person()
            assert key_word in table_result, f'The person with key word {key_word}, did not find in table result {table_result}'

        def test_web_table_update_person_info(self, driver): #TODO make the test change different parameters
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_a_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_searched_person()
            assert age in row, f'The person card has not been changed'


        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_new_person()[3]
            web_tables_page.search_a_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()
            assert text == "No rows found"


        def test_web_table_change_cout_row(self, driver): #with BUG
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 50, 50, 100], "Number of rows in the table has not been changend or has not been changed incorrectly"

    class TestButtonPage:

        def test_different_click_on_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert double == "You have done a double click", "The double click button was not clicked"
            assert right == "You have done a right click", "The right click button was not clicked"
            assert click == "You have done a dynamic click", "The dynamic click button was not clicked"
