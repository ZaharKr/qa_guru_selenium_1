import pytest


@pytest.mark.login
@pytest.mark.smoke
def test_success_login(login_page):
    login_page.login("user1", "password1")
    assert login_page.is_success()
    assert "user1" in login_page.welcome_text()


@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("user1", "wrongpass", "Wrong login or password"),
        ("unknown", "password1", "Wrong login or password"),
        ("", "", "Login and password are required"),
        ("user1", "", "Password is required"),
        ("", "password1", "Login is required"),
    ],
    ids=["wrong-pass", "unknown-user", "empty-both", "empty-pass", "empty-login"],
)
def test_login_errors(login_page, username, password, expected):
    login_page.login(username, password)
    assert expected in login_page.error_text()
    assert not login_page.is_success()


@pytest.mark.login
@pytest.mark.skip(reason="демо pytest.mark.skip — сценарий logout уже покрыт в lesson_2")
def test_logout_skipped(login_page):
    login_page.login("user1", "password1")
    assert False, "не должны сюда попасть"


@pytest.mark.login
@pytest.mark.skipif(True, reason="демо skipif — условный пропуск")
def test_skipif_demo():
    assert False
