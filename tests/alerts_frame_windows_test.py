from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new tab hasn't opened or incorrect tab has opened"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new window hasn't opened or incorrect window has opened"

    class TestAlertsPage:

        def test_see_alert(self,driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert() #TODO Combine methods into one "switch to alert" and move to BasePage
            assert alert_text == "You clicked a button", "Alert didn't show up"

        def test_see_alert_appear_5_sec(self,driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert didn't show up after 5 seconds"

        def test_confirm_alert(self, driver): # TODO make random click OK \ Cancel
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Alert didn't show up OR text is incorrect"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
#            assert alert_text == f"You entered {text}"
            assert text in alert_text, "Alert didn't show up OR text is incorrect"

    class TestFramesPage:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_frame1 = frames_page.check_frame("frame1")
            result_frame2 = frames_page.check_frame("frame2")
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame doesn't exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame doesn't exist"

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame", "Nested frame doesn't exist"
            assert child_text == "Child Iframe", "Nested frame doesn't exist"

    class TestModalDialogsPage:

        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            modal_small, modal_large = modal_dialogs_page.check_modal_dialogs()
            assert modal_small[0] == "Small Modal", f'Should be "Small Modal", but was {modal_small[0]}'
            assert modal_large[0] == "Large Modal", f'Should be "Large Modal", but was {modal_large[0]}'
            assert modal_large[1] > modal_small[1], (f'length large modal text is {modal_large[1]}, '
                                                     f'length small modal text is {modal_small[1]} ')
