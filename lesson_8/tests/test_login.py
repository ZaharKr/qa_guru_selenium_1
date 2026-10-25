import allure
import pytest


@allure.epic("one-page-form")
@allure.feature("Login")
@allure.title("Успешный логин")
@pytest.mark.login
@pytest.mark.smoke
def test_success_login(login_page):
    with allure.step("Логин user1/password1"):
        login_page.login("user1", "password1")
    with allure.step("Проверка success"):
        assert login_page.is_success()
        assert "user1" in login_page.welcome_text()


@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize(
    "login, password, error_message",
    [
        ("johndoe@gmail.com", "JoH!?Do1+", "Wrong login or password"),
        ("", "", "Login and password are required"),
        ("", "JoH!?Do1+", "Login is required"),
        ("johndoe", "", "Password is required"),
        ("user1", "wrongpass", "Wrong login or password"),
    ],
    ids=[
        "unregistered_user",
        "empty_fields",
        "empty_login",
        "empty_password",
        "wrong_pass",
    ],
)
def test_unsuccessful_login(login_page, login, password, error_message):
    login_page.fill_login(login).fill_password(password).click_login()
    assert error_message in login_page.error_text()
    assert not login_page.is_success()
