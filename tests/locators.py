from selenium.webdriver.common.by import By


class Registration:
    REGISTER = (By.LINK_TEXT, 'Зарегистрироваться')  # кнопка регистрации
    REGISTRATION_PAGE_NAME = (
        By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  # страница регистрации, поле имени
    REGISTRATION_PAGE_EMAIL = (
        By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  # страница регистрации, поле email
    REGISTRATION_PAGE_PASSWORD = (
        By.XPATH,
        "//label[text()='Пароль']/following-sibling::input[@type='password']")  # страница регистрации, поле пароля
    REGISTRATION_PAGE_REGISTER_BUTTON = (
        By.XPATH, "//button[text()='Зарегистрироваться']")  # страница регистрации, кнопка "Зарегистрироваться"
    REGISTRATION_PAGE_INCORRECT_PASSWORD_ERROR = (
        By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  # сообщение об ошибке "Некорректный пароль"


class Login:
    PERSONAL_ACCOUNT = (By.LINK_TEXT, 'Личный Кабинет')  # главная страница, кнопка личного кабинета/страницы входа
    LOGIN_EMAIL = (
        By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # страница входа, поле email
    LOGIN_PASSWORD = (
        By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")  # страница входа, поле пароля
    LOGIN_BUTTON = (By.XPATH, "//*[contains(text(),'Войти')]")  # страница входа, кнопка входа
    ENTER_ACCOUNT = (
        By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # главная страница, фиолетовая кнопка входа в аккаунт
    WHEN_LOGGED_IN_PUT_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Оформить заказ')]")  # кнопка "Оформить заказ" на главной при авторизированном аккаунте
    WHEN_LOGGED_IN_PERSONAL_ACCOUNT_PAGE_SETTINGS = (
        By.XPATH,
        "//*[contains(text(), 'В этом разделе вы можете изменить свои персональные данные')]")  # надпись в личном кабинете при авторизированном аккаунте
    LOGIN_LINK = (By.XPATH,
                  "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")  # ссылка на вход на странице восстановления пароля или регистрации
    PURPLE_LOGIN_BUTTON_ON_LOGIN_PAGE = (
        By.XPATH,
        "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")  # фиолетовая кнопка входа на странице логина
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")  # кнопка логаута
    LOGIN_PAGE_LOGIN_TEXT = (By.XPATH, "//*[contains(text(),'Вход')]")  # текст "Вход" на странице входа


class Constructor:
    INACTIVE_BUNS_SECTION_CHANGE_BUTTON = (By.XPATH,
                                           "//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'current'))]//span[text()='Булки']")  # конструктор бургеров, кнопка переключения на раздел "Булки"
    BUNS_SECTION_TEXT = (By.XPATH, "//span[text()='Булки']")  # конструктор бургеров, текст "Булки"
    SAUCE_SECTION_CHANGE_BUTTON = (By.XPATH,
                                   "//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'current'))]//span[text()='Соусы']")  # конструктор бургеров, кнопка переключения на раздел "Соусы"

    SAUCE_SECTION_TEXT = (By.XPATH, "//span[text()='Соусы']")  # конструктор бургеров, текст "Соусы"
    FILLING_SECTION_CHANGE_BUTTON = (By.XPATH,
                                     "//div[contains(@class, 'tab_tab__1SPyG') and not(contains(@class, 'current'))]//span[text()='Начинки']")  # конструктор бургеров, кнопка переключения на раздел "Начинки"

    FILLING_SECTION_TEXT = (By.XPATH, "//span[text()='Начинка']")  # конструктор бургеров, текст "Начинки"
    BUNS_ACTIVE_SECTION = (
        By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')][.='Булки']")  # активная вкладка "Булки"
    SAUCE_ACTIVE_SECTION = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']")  # активная вкладка "Соусы"
    FILLING_ACTIVE_SECTION = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']")  # активная вкладка "Начинки"
    MAIN_PAGE_CONSTRUCTOR_LINK = (
        By.XPATH,
        '//*[contains(text(), "Конструктор")]' and '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')  # ссылка "Конструктор" в хедере

    MAIN_PAGE_STELLAR_BURGERS_LOGO = (
        By.XPATH, '//*[@id="root"]/div/header/nav/div' and "//*[@class='AppHeader_header__logo__2D0X2']")  # лого Stellar Burgers в хедере
