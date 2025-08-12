import random
import time
from faker import Faker

from selenium.webdriver.support import expected_conditions as ec

from locators import HeaderLocators, CreateAdPageLocators, UserPageLocators
from config import Advertisement


class TestCreateAd:

    def test_create_ad_by_an_unauthorized_user(
            self,
            driver,
            open_main_page,
            waiting
    ):
        driver.find_element(*HeaderLocators.CREATE_AD_BUTTON).click()
        waiting.until(ec.visibility_of_element_located((CreateAdPageLocators.TITLE_POPUP_LOGIN_FOR_CREATE_AD)))

        assert driver.find_element(
            *CreateAdPageLocators.TITLE_POPUP_LOGIN_FOR_CREATE_AD).text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_create_ad_by_an_authorized_user(
            self,
            driver,
            waiting,
            user_login
    ):
        fake = Faker('ru')

        driver.find_element(*HeaderLocators.CREATE_AD_BUTTON).click()
        waiting.until(ec.visibility_of_element_located((CreateAdPageLocators.AD_TITLE_INPUT)))

        ad_title = f'Объявление "{fake.word()}"'
        driver.find_element(*CreateAdPageLocators.AD_TITLE_INPUT).send_keys(ad_title)
        driver.find_element(*CreateAdPageLocators.PRODUCT_DESCRIPTION_INPUT).send_keys(fake.text())
        driver.find_element(*CreateAdPageLocators.PRICE_INPUT).send_keys(fake.random_int(min=0, max=999999))

        driver.find_element(*CreateAdPageLocators.CATEGORY_DROPDOWN_MENU).click()
        random_category = random.choice(Advertisement.categories)
        category_locator = CreateAdPageLocators.get_category_locator(random_category)
        driver.find_element(*category_locator).click()

        driver.find_element(*CreateAdPageLocators.CITY_DROPDOWN_MENU).click()
        random_city = random.choice(Advertisement.cities)
        city_locator = CreateAdPageLocators.get_city_locator(random_city)
        driver.find_element(*city_locator).click()

        random_radiobutton = random.choice(Advertisement.radiobuttons)
        if random_radiobutton == 'Б/У':
            driver.find_element(*CreateAdPageLocators.CONDITION_RADIO_BUTTON).click()

        driver.find_element(*CreateAdPageLocators.PUBLISH_BUTTON).click()
        waiting.until(ec.visibility_of_element_located((CreateAdPageLocators.SEARCH_INPUT)))
        driver.find_element(*HeaderLocators.AVATAR_ICON).click()

        waiting.until(ec.visibility_of_element_located((UserPageLocators.PAGINATION_BUTTON)))

        while True:
            pagination_right_button = driver.find_element(*UserPageLocators.PAGINATION_BUTTON)
            if pagination_right_button.get_attribute('disabled') is not None:
                break
            else:
                pagination_right_button.click()

        # Info: Пришлось поставить time.sleep, так как не хватило идей понять,
        #  почему иногда в тесте ad_title_text беретя с предпоследней страницы объявлений.
        #  Установка ожидания не помогает
        time.sleep(1)

        ad_title_text = driver.find_element(*UserPageLocators.LAST_AD_CARD_TITLE).text
        assert ad_title_text == ad_title
