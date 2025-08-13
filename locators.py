from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGIN_REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Вход и регистрация"]')
    CREATE_AD_BUTTON = (By.XPATH, '//button[text()="Разместить объявление"]')
    PROFILE_NAME = (By.XPATH, '//div[@class="columnSmall"]/h3')
    AVATAR_ICON = (By.XPATH, '//button[@class="circleSmall"]')
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')


class MainPageLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '.input_inputDefaultSearch__EKhe3')


class RegistrationPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="submitPassword"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Создать аккаунт"]')
    ERROR_INPUT = (By.CSS_SELECTOR, '.input_inputError__fLUP9')
    EMAIL_TEXT_ERROR = (By.XPATH, '//input[@name="email"]/following::span[@class="input_span__yWPqB"]')


class AuthorizationPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')


class CreateAdPageLocators:
    TITLE_POPUP_LOGIN_FOR_CREATE_AD = (By.XPATH, '//form[@class="popUp_shell__LuyqR"]//h1')
    AD_TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    PRODUCT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'textarea[name="description"]')
    PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')
    CATEGORY_DROPDOWN_MENU = (By.XPATH, '//input[@name="category"]/following-sibling::button')
    CITY_DROPDOWN_MENU = (By.XPATH, '//input[@name="city"]/following-sibling::button')
    CONDITION_RADIO_BUTTON = (By.XPATH,
                              '//input[@value="Б/У"]/ancestor::div[contains(@class, "radioUnput_shell")]//div[@class="radioUnput_inputRegular__FbVbr"]')
    PUBLISH_BUTTON = (By.XPATH, '//button[text()="Опубликовать"]')
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Я хочу купить...']")

    @staticmethod
    def get_category_locator(category_name):
        return (By.XPATH, f"//button[.//span[text()='{category_name}']]")

    @staticmethod
    def get_city_locator(city_name):
        return (By.XPATH, f"//button[.//span[text()='{city_name}']]")


class UserPageLocators:
    PAGINATION_BUTTON = (By.XPATH, '//button[@class="arrowButton arrowButton--right undefined"]')
    LAST_AD_CARD_TITLE = (By.XPATH, '//div[@class="card"][last()]//div[@class="about"]/h2')
