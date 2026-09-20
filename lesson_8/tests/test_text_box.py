import pytest


TEXT_BOX_CASES = [
    pytest.param(
        {
            "name": "John Doe",
            "email": "john_doe@gmail.com",
            "cur": "740 Route 202 Middletown, NY 10940",
            "perm": "9476 Virginia Avenue South Richmond Hill, NY 11419",
        },
        id="john",
    ),
    pytest.param(
        {
            "name": "Иван Иванов",
            "email": "ivan@mail.ru",
            "cur": "ул. Ленина, 1",
            "perm": "ул. Пушкина, 2",
        },
        id="ivan",
    ),
]


@pytest.mark.textbox
@pytest.mark.smoke
@pytest.mark.parametrize("case", TEXT_BOX_CASES)
def test_fill_text_box(text_box_page, case):
    (
        text_box_page.fill_name(case["name"])
        .fill_email(case["email"])
        .fill_current_address(case["cur"])
        .fill_permanent_address(case["perm"])
        .submit()
    )
    result = text_box_page.get_output()
    assert result is not None
    assert result["Name"] == case["name"]
    assert result["Email"] == case["email"]
    assert result["Current Address"] == case["cur"]
    assert result["Permananet Address"] == case["perm"]


@pytest.mark.textbox
@pytest.mark.regression
@pytest.mark.parametrize(
    "email",
    ["?", "plainaddress", "john@@example.com"],
    ids=["question", "plain", "double-at"],
)
def test_invalid_email_hides_result(text_box_page, email):
    (
        text_box_page.fill_name("John Doe")
        .fill_email(email)
        .fill_current_address("NY")
        .fill_permanent_address("NY")
        .submit()
    )
    assert text_box_page.is_result_hidden() or not text_box_page.is_email_valid()


@pytest.mark.textbox
@pytest.mark.regression
def test_sql_inject_username_field(text_box_page):
    (
        text_box_page.fill_name("'1' OR '1'='1")
        .fill_email("john_doe@gmail.com")
        .fill_current_address("NY")
        .fill_permanent_address("NY")
        .submit()
    )
    result = text_box_page.get_output()
    assert result is not None
    assert result["Name"] == "'1' OR '1'='1"
