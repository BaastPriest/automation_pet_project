import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage

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


