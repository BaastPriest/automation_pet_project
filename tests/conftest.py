import pytest, sys, os, tempfile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    # temporary directory for profile
    with tempfile.TemporaryDirectory() as profile_path:
        chrome_options.add_argument(f"user-data-dir={profile_path}")

    # prevents an error in the final block if the driver was not created successfully
    driver = None

    # Run ChromeDriver
    try:
        driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        yield driver
    except WebDriverException as e:
        pytest.fail(f"Ошибка при запуске ChromeDriver: {e}")
    finally:
        if driver: # check if it was created successfully (not equal to None)
            driver.quit()
