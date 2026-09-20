import pytest

from tests.conftest import POSITIVE_CASES


@pytest.mark.textbox
@pytest.mark.smoke
@pytest.mark.parametrize("filled_output", POSITIVE_CASES, indirect=True)
def test_positive_submission(filled_output):
    output, name, email, cur_addr, perm_addr = filled_output
    assert output is not None
    assert output["name"] == name.strip()
    assert output["email"] == email.strip()
    assert output["cur_addr"] == cur_addr.strip()
    assert output["perm_addr"] == perm_addr.strip()


@pytest.mark.textbox
@pytest.mark.regression
@pytest.mark.parametrize(
    "email, should_accept",
    [
        ("plainaddress", False),
        ("@no-local-part.com", False),
        ("john@@example.com", False),
        ("john@example.com", True),
        # Chrome часто считает john.doe@com валидным — фиксируем факт
        ("john.doe@com", True),
    ],
    ids=["no-at", "no-local", "double-at", "valid", "short-tld"],
)
def test_email_validity(text_box_page, email, should_accept):
    text_box_page.fill_form(name="Test", email=email).submit()
    output = text_box_page.get_output_data()
    valid = text_box_page.is_email_valid()
    if should_accept:
        assert valid and output is not None
    else:
        assert (not valid) or output is None


@pytest.mark.textbox
@pytest.mark.xfail(reason="демо xfail: форма сейчас принимает пустой email", strict=False)
@pytest.mark.regression
def test_xfail_empty_email_rejected(text_box_page):
    output = text_box_page.fill_form(name="No Email", email="").submit().get_output_data()
    assert output is None


@pytest.mark.textbox
@pytest.mark.regression
def test_empty_form(text_box_page):
    text_box_page.submit()
    output = text_box_page.get_output_data()
    if output is not None:
        assert output["name"] == ""
        assert output["email"] == ""


@pytest.mark.textbox
@pytest.mark.smoke
def test_partial_name_only(text_box_page):
    output = text_box_page.fill_form(name="Only Name").submit().get_output_data()
    assert output is not None
    assert output["name"] == "Only Name"
