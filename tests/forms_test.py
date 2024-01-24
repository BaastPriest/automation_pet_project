from pages.forms_page import FormsPage


class TestForms:
    class TestFormsPage:
        def test_fill_form(self, driver):
            forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
            forms_page.open()
            person_info = forms_page.fill_form_fields()
            result = forms_page.form_result()
            assert [person_info.first_name + " " + person_info.last_name, person_info.email] == [result[0], result[1]],\
                "The form has not been filled"

        def test_fill_form_with_random_value(self, driver):
            forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
            forms_page.open()
            person_info = forms_page.fill_form_fields_with_random_value()
            result = forms_page.form_result()
            assert [person_info.first_name + " " + person_info.last_name, person_info.email] == [result[0], result[1]],\
                "The form has not been filled"
