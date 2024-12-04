from pages.base_page import BasePage
import allure
from utils.config import Config  # Add this import

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator('[name="username"]')
        self.password_input = page.locator('[name="password"]')
        self.login_button = page.locator('button[type="submit"]')

    def navigate(self):
        """Navigate to login page"""
        with allure.step("Navigating to login page"):
            self.page.goto(f"{Config.BASE_URL}/web/index.php/auth/login")
            self.page.wait_for_load_state("networkidle")

    @allure.step("Login with credentials")
    def login(self, username: str, password: str):
        self.logger.info(f"Logging in as user: {username}")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()