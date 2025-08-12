from selenium.webdriver.support import expected_conditions as ec

from locators import AuthorizationPageLocators, HeaderLocators
from config import Common, User


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

        # ОР: После авторизации должен быть редирект на главную страницу https://qa-desk.stand.praktikum-services.ru/
        # ФР: URL не меняется, хотя пользователь залогинен - тест упадет на следующем шаге.
        # Info: Для проверки логина без смены URL закомментируй строчку assert driver.current_url == Common.URL
        assert driver.current_url == Common.URL
        assert driver.find_element(*HeaderLocators.PROFILE_NAME).text == 'User.'
        assert driver.find_element(*HeaderLocators.AVATAR_ICON).is_displayed()
