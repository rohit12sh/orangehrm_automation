from playwright.sync_api import Page
import allure
from utils.logger import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger()

    def check_accessibility(self):
        """Run accessibility audit on current page"""
        with allure.step("Running accessibility check"):
            from axe_selenium_python import Axe
            axe = Axe(self.page)
            # Run axe accessibility audit
            results = axe.execute()
            violations = results["violations"]
            
            if violations:
                for violation in violations:
                    allure.attach(
                        str(violation),
                        name=f"Accessibility Violation: {violation['id']}",
                        attachment_type=allure.attachment_type.TEXT
                    )
            return violations
        