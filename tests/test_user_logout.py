from selenium.webdriver.support import expected_conditions as ec

from locators import HeaderLocators


class TestUserLogout:

    def test_user_logout(
            self,
            driver,
            waiting,
            user_login
    ):
        driver.find_element(*HeaderLocators.EXIT_BUTTON).click()
        waiting.until(ec.visibility_of_element_located((HeaderLocators.LOGIN_REGISTRATION_BUTTON)))

        assert not driver.find_elements(*HeaderLocators.PROFILE_NAME)
        assert not driver.find_elements(*HeaderLocators.AVATAR_ICON)
        assert driver.find_element(*HeaderLocators.LOGIN_REGISTRATION_BUTTON).is_displayed()
