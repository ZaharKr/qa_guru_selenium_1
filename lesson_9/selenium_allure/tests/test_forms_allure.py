import allure
import pytest


@allure.epic("QA Guru one-page-form")
@allure.feature("Text Box")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.textbox
@allure.title("Заполнение Text Box валидными данными")
def test_text_box_positive(text_box_page):
    with allure.step("Заполняем форму"):
        (
            text_box_page.fill_name("John Doe")
            .fill_email("john@example.com")
            .fill_current_address("NY")
            .fill_permanent_address("LA")
            .submit()
        )
    with allure.step("Проверяем output"):
        result = text_box_page.get_output()
        allure.attach(str(result), name="output", attachment_type=allure.attachment_type.TEXT)
        assert result is not None
        assert result["Name"] == "John Doe"
        assert result["Email"] == "john@example.com"


@allure.epic("QA Guru one-page-form")
@allure.feature("Login")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.login
@allure.title("Успешный логин user1")
def test_login_success(login_page):
    with allure.step("Логин user1 / password1"):
        login_page.login("user1", "password1")
    with allure.step("Проверяем welcome"):
        assert login_page.is_success()
        assert "user1" in login_page.welcome_text()


@allure.epic("QA Guru one-page-form")
@allure.feature("Login")
@allure.story("Негативные сценарии")
@pytest.mark.login
@pytest.mark.parametrize(
    "login, password, expected",
    [
        ("user1", "wrongpass", "Wrong login or password"),
        ("", "", "Login and password are required"),
    ],
    ids=["wrong-pass", "empty"],
)
@allure.title("Ошибки логина")
def test_login_errors(login_page, login, password, expected):
    allure.dynamic.parameter("login", login or "<empty>")
    allure.dynamic.parameter("password", password or "<empty>")
    with allure.step("Отправляем форму"):
        login_page.login(login, password)
    with allure.step("Проверяем текст ошибки"):
        assert expected in login_page.error_text()
