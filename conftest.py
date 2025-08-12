import pytest
import random

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators import HeaderLocators, AuthorizationPageLocators
from config import Common, User


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def waiting(driver):
    return WebDriverWait(driver, 3)

@pytest.fixture()
def open_main_page(driver):
    driver.get(Common.URL)

@pytest.fixture()
def click_login_registration_button(driver, waiting):
    driver.find_element(*HeaderLocators.LOGIN_REGISTRATION_BUTTON).click()
    waiting.until(ec.visibility_of_element_located((AuthorizationPageLocators.LOGIN_BUTTON)))

@pytest.fixture()
def click_no_account_button(driver):
    driver.find_element(*AuthorizationPageLocators.NO_ACCOUNT_BUTTON).click()

@pytest.fixture()
def generate_email(driver):
    email = f'user{random.randint(0000, 9999)}@test.com'
    return email

@pytest.fixture()
def generate_password(driver):
    password = f'{random.randint(0000, 9999)}'
    return password

@pytest.fixture()
def user_login(driver, waiting, open_main_page, click_login_registration_button):
    driver.find_element(*AuthorizationPageLocators.EMAIL_INPUT).send_keys(User.EMAIL)
    driver.find_element(*AuthorizationPageLocators.PASSWORD_INPUT).send_keys(User.PASSWORD)
    driver.find_element(*AuthorizationPageLocators.LOGIN_BUTTON).click()
    waiting.until(ec.visibility_of_element_located((HeaderLocators.PROFILE_NAME)))