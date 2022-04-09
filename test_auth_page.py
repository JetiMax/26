import time
from pages.auth_page import AuthPage



def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("jetimax@yandex.ru")
    page.enter_pass("1725maksim")
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() != '/all_pets', "login error"

    time.sleep(5)  # задержка для учебных целей
