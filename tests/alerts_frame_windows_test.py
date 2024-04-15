from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


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