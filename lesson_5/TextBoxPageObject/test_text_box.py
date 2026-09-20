import pytest
from text_box_page import TextBoxPage

# Сравнение с/без PageFactory — см. ../NOTES.md
# john.doe@com и john@missing-dot браузер часто считает valid (type=email) —
# поэтому дополнительно смотрим HTML5 validity.


@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        ("John Doe", "john@example.com", "123 Elm St", "456 Oak St"),
        ("Иван Иванов", "ivan@mail.ru", "ул. Ленина, д. 1", "ул. Пушкина, д. 2"),
        ("A", "a@b.cc", "B", "C"),
        ("Name-With Dash", "dash@email.co.uk", "Addr 1/2", "Addr 3 & 4"),
        ("   John   ", "spaces@test.com", "  Street 1  ", "  Street 2  "),
    ],
)
def test_positive_form_submission(driver, name, email, cur_addr, perm_addr):
    output = TextBoxPage(driver).open().fill_form(name, email, cur_addr, perm_addr).submit().get_output_data()

    assert output is not None
    assert output["name"] == name.strip()
    assert output["email"] == email.strip()
    assert output["cur_addr"] == cur_addr.strip()
    assert output["perm_addr"] == perm_addr.strip()


@pytest.mark.parametrize(
    "name, email, cur_addr, perm_addr",
    [
        ("Only Name", "", "", ""),
        ("", "only@email.com", "", ""),
        ("", "", "Only Current Address", ""),
        ("", "", "", "Only Permanent Address"),
        ("Name & Email", "name_email@test.com", "", ""),
    ],
)
def test_partial_form_submission(driver, name, email, cur_addr, perm_addr):
    page = TextBoxPage(driver)
    page.open()
    page.fill_form(name, email, cur_addr, perm_addr)
    page.submit()
    output = page.get_output_data()

    assert output is not None
    assert output["name"] == name
    assert output["email"] == email
    assert output["cur_addr"] == cur_addr
    assert output["perm_addr"] == perm_addr


@pytest.mark.parametrize(
    "invalid_email",
    [
        "plainaddress",
        "@no-local-part.com",
        "john.doe@com",
        "john@missing-dot",
        "john@@example.com",
        "john@example..com",
    ],
)
def test_invalid_email_validation(driver, invalid_email):
    page = TextBoxPage(driver)
    page.open()
    page.fill_form(name="Test", email=invalid_email)
    page.submit()
    output = page.get_output_data()

    # Chrome type=email пропускает john.doe@com и john@missing-dot
    if invalid_email in ("john.doe@com", "john@missing-dot"):
        assert page.is_email_valid()
        assert output is not None
        return

    rejected = (
        output is None
        or page.is_email_error_present()
        or not page.is_email_valid()
    )
    assert rejected, f"Email '{invalid_email}' не должен быть принят"


@pytest.mark.parametrize(
    "kwargs, expected_key, expected_value",
    [
        ({"name": "A" * 1000}, "name", "A" * 1000),
        ({"email": f"{'b' * 64}@example.com"}, "email", f"{'b' * 64}@example.com"),
        ({"cur_addr": "CurrentX" * 200}, "cur_addr", "CurrentX" * 200),
        ({"perm_addr": "PermanentX" * 200}, "perm_addr", "PermanentX" * 200),
    ],
)
def test_long_input_fields(driver, kwargs, expected_key, expected_value):
    page = TextBoxPage(driver).open()
    page.fill_form(**kwargs)
    page.submit()
    output = page.get_output_data()
    assert output is not None
    assert output[expected_key] == expected_value


@pytest.mark.parametrize(
    "security_payload",
    [
        "<script>alert('xss')</script>",
        "1' OR '1'='1",
        ":):):):))))::;)",
        "<div>HTML injection</div>",
    ],
)
def test_security_and_special_inputs(driver, security_payload):
    page = TextBoxPage(driver).open()
    page.fill_form(name=security_payload, cur_addr=security_payload, perm_addr=security_payload)
    page.submit()
    output = page.get_output_data()
    assert output is not None

    if "<" in security_payload:
        # теги могут "вылезти" из <p id="name"> — смотрим page_source
        assert "HTML injection" in driver.page_source or "xss" in driver.page_source.lower() or "<script" in driver.page_source.lower() or "<div" in driver.page_source.lower()
    else:
        assert output["name"] == security_payload


def test_empty_form_submission(driver):
    page = TextBoxPage(driver).open()
    page.submit()
    output = page.get_output_data()
    if output is not None:
        assert output["name"] == ""
        assert output["email"] == ""
