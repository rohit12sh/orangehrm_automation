import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from utils.logger import setup_logger
import allure
from datetime import datetime

def pytest_configure(config):
    setup_logger()
    config.option.allure_report_dir = "reports/allure-results"

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context(
        record_video_dir="reports/videos/",
        viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()
    
    yield page
    
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"reports/screenshots/failure_{request.node.name}_{timestamp}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
    
    context.close()