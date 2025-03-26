from src.config import Config
from src.locators.locators import EnterLocators
from conftest import driver


class TestConstructorSection:

    def test_go_to_the_breads_section(self, driver):
        driver.get(Config.URL)
        driver.find_element(*EnterLocators.SAUCES_TAB).click()
        driver.find_element(*EnterLocators.BREADS_TAB).click()
        assert EnterLocators.CURRENT_BREADS_TAB, "Another tab is selected"
        driver.quit()

    def test_go_to_the_sauces_section(self, driver):
        driver.get(Config.URL)
        driver.find_element(*EnterLocators.SAUCES_TAB).click()
        assert EnterLocators.CURRENT_SAUCES_TAB, "Another tab is selected"
        driver.quit()

    def test_go_to_the_toppings_section(self, driver):
        driver.get(Config.URL)
        driver.find_element(*EnterLocators.TOPPINGS_TAB).click()
        assert EnterLocators.CURRENT_TOPPINGS_TAB, "Another tab is selected"
        driver.quit()
