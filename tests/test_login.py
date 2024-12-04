import pytest
import allure
from pages.login_page import LoginPage
from utils.config import Config

@allure.feature("Authentication")
@allure.story("Login")
class TestLogin:
    @allure.title("Verify successful login with valid credentials")
    @pytest.mark.smoke
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        assert page.url.endswith("/dashboard/index")
