from playwright.sync_api import Page
import allure

class SideMenu:
    def __init__(self, page: Page):
        self.page = page
        self.menu = page.locator('.oxd-sidepanel')

    @allure.step("Navigate to {menu_item}")
    def navigate_to(self, menu_item: str):
        self.menu.locator(f"span:text-is('{menu_item}')").click()
