from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code() # Метод перехватит промо-алерт и напечатает код в консоль
    
    # Финальные проверки структуры (ожидаемый результат)
    page.should_be_success_message()
    page.should_be_basket_total_matches_price()