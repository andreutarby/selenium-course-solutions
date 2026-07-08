from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def should_be_success_message(self):
        # Проверяем, что имя товара в алерте совпадает с реальным именем товара
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == alert_name, f"Expected product name '{product_name}', got '{alert_name}'"

    def should_be_basket_total_matches_price(self):
        # Проверяем, что цена в сообщении о корзине совпадает с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_price, f"Expected basket price '{product_price}', got '{basket_price}'"