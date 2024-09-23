from datetime import datetime
import allure, shutil, pytest, os, tempfile, sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="function")
def driver(request):
    chrome_options = Options()
    # temporary directory
    profile_path = tempfile.mkdtemp()

    # options for CI/CD
    chrome_options.add_argument("--headless") #Launches Chrome in the background, without displaying the interface
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = None
    try:
        chrome_options.add_argument(f"user-data-dir={profile_path}")
        driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver

    except WebDriverException as e:
        pytest.fail(f"Error on startup ChromeDriver: {e}")

    finally:
        if driver:
            if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
                attach = driver.get_screenshot_as_png()
                allure.attach(attach,
                              name=f"Screenshot {datetime.today()}",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(driver.current_url, name="Current URL",
                              attachment_type=allure.attachment_type.TEXT)
            driver.quit()
        if profile_path and os.path.exists(profile_path):
            shutil.rmtree(profile_path)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # returns a report object after each test
    outcome = yield
    rep = outcome.get_result()

    # Assign report to current test to access it in fixture
    if rep.when == "call":
        item.rep_call = rep
