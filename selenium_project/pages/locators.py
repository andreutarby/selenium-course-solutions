from selenium.webdriver.common.by import By

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    
    # Локаторы для сообщений об успешном добавлении (алерты на самой странице)
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1) strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-info strong")