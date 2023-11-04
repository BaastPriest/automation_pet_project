import time

from pages.elements_page import TextBoxPage, CheckBoxPage


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
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, f'Expected selected checkboxes {input_checkbox} but actual {output_result}'
