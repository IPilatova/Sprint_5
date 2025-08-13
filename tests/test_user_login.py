from selenium.webdriver.support import expected_conditions as ec

from locators import AuthorizationPageLocators, HeaderLocators, MainPageLocators
from config import User


class TestUserLogin:

    def test_success_user_login(
            self,
            driver,
            waiting,
            open_main_page,
            click_login_registration_button
    ):
        driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT).send_keys(User.EMAIL)
        driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON).click()
        waiting.until(ec.visibility_of_element_located((HeaderLocators.PROFILE_NAME)))

        assert driver.find_element(*MainPageLocators.SEARCH_INPUT).is_displayed()
        assert driver.find_element(*HeaderLocators.PROFILE_NAME).text == 'User.'
        assert driver.find_element(*HeaderLocators.AVATAR_ICON).is_displayed()
