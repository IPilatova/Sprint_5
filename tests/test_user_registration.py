import pytest

from selenium.webdriver.support import expected_conditions as ec

from locators import RegistrationPageLocators, HeaderLocators, MainPageLocators
from config import User


class TestUserRegistration:

    def test_success_user_registration(
            self,
            driver,
            waiting,
            open_main_page,
            click_login_registration_button,
            click_no_account_button,
            generate_email,
            generate_password
    ):
        driver.find_element(
            *RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(generate_password)
        driver.find_element(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(generate_password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()
        waiting.until(ec.visibility_of_element_located((HeaderLocators.PROFILE_NAME)))

        assert driver.find_element(*MainPageLocators.SEARCH_INPUT).is_displayed()
        assert driver.find_element(*HeaderLocators.PROFILE_NAME).text == 'User.'
        assert driver.find_element(*HeaderLocators.AVATAR_ICON).is_displayed()

    @pytest.mark.parametrize(
        'email',
        ['user111@testcom', 'user111test.com', 'user111testcom', 'user111.test@com']
    )
    def test_user_registration_with_email_not_by_mask(
            self,
            driver,
            waiting,
            open_main_page,
            click_login_registration_button,
            click_no_account_button,
            generate_password,
            email
    ):
        driver.find_element(
            *RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(generate_password)
        driver.find_element(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(generate_password)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        waiting.until(ec.visibility_of_element_located((RegistrationPageLocators.ERROR_INPUT)))

        elements = driver.find_elements(*RegistrationPageLocators.ERROR_INPUT)
        assert len(elements) == 3
        for index, element in enumerate(elements, start=1):
            border_color = element.value_of_css_property('border-color')
            assert border_color == 'rgb(255, 105, 114)'

        assert driver.find_element(*RegistrationPageLocators.EMAIL_TEXT_ERROR).text == 'Ошибка'

    def test_user_registration_an_existing_user(
            self,
            driver,
            waiting,
            open_main_page,
            click_login_registration_button,
            click_no_account_button
    ):
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(User.EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*RegistrationPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(User.PASSWORD)
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        waiting.until(ec.visibility_of_element_located((RegistrationPageLocators.ERROR_INPUT)))

        elements = driver.find_elements(*RegistrationPageLocators.ERROR_INPUT)
        assert len(elements) == 3
        for index, element in enumerate(elements, start=1):
            border_color = element.value_of_css_property('border-color')
            assert border_color == 'rgb(255, 105, 114)'

        assert driver.find_element(*RegistrationPageLocators.EMAIL_TEXT_ERROR).text == 'Ошибка'
