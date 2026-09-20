import pytest

from pages.registration_page import RegistrationPage


REG_CASES = [
    {
        "first": "John",
        "last": "Doe",
        "email": "johndoe@gmail.com",
        "gender": "Male",
        "phone": "9181234567",
        "year": "1994",
        "month": "8",
        "day": "14",
        "subjects": ("Computer Science",),
        "hobbies": ("Reading",),
        "address": "NYC",
        "state": "NCR",
        "city": "Delhi",
    },
    {
        "first": "Anna",
        "last": "Smirnova",
        "email": "anna@mail.ru",
        "gender": "Female",
        "phone": "9001112233",
        "year": "1995",
        "month": "11",
        "day": "05",
        "subjects": ("Maths", "English"),
        "hobbies": ("Sports", "Music"),
        "address": "Москва",
        "state": "NCR",
        "city": "Noida",
    },
]


@pytest.mark.registration
@pytest.mark.smoke
def test_fill_only_required_fields(registration_page):
    (
        registration_page.set_firstname("John")
        .set_lastname("Doe")
        .set_gender("Male")
        .set_phone("9181234567")
        .submit_form()
    )
    text = registration_page.result_text()
    assert "John Doe" in text
    assert "Male" in text
    assert "9181234567" in text


@pytest.mark.registration
@pytest.mark.regression
@pytest.mark.parametrize("case", REG_CASES, ids=["john", "anna"])
def test_fill_all_fields(registration_page, case, tmp_path):
    picture = tmp_path / "students.jpg"
    picture.write_bytes(b"fake-image")

    (
        registration_page.set_firstname(case["first"])
        .set_lastname(case["last"])
        .set_email(case["email"])
        .set_gender(case["gender"])
        .set_phone(case["phone"])
        .set_birthdate(case["year"], case["month"], case["day"])
        .set_subjects(*case["subjects"])
        .set_hobbies(*case["hobbies"])
        .upload_picture(str(picture))
        .set_address(case["address"])
        .set_state_city(case["state"], case["city"])
        .submit_form()
    )

    text = registration_page.result_text()
    assert f"{case['first']} {case['last']}" in text
    assert case["email"] in text
    assert case["gender"] in text
    assert case["phone"] in text
    assert RegistrationPage.format_birth(case["year"], case["month"], case["day"]) in text
    for subject in case["subjects"]:
        assert subject in text
    for hobby in case["hobbies"]:
        assert hobby in text
    assert "students.jpg" in text
    assert case["address"] in text
    assert case["state"] in text and case["city"] in text
