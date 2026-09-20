import pytest


POSITIVE_CASES = [
    ("John Doe", "john@example.com", "123 Elm St", "456 Oak St"),
    ("Иван Иванов", "ivan@mail.ru", "ул. Ленина, д. 1", "ул. Пушкина, д. 2"),
    pytest.param(("A", "a@b.cc", "B", "C"), id="min-length"),
]


@pytest.fixture
def filled_output(text_box_page, request):
    """Factory-style: данные кейса приходят через indirect parametrize."""
    name, email, cur_addr, perm_addr = request.param
    output = (
        text_box_page.fill_form(name, email, cur_addr, perm_addr)
        .submit()
        .get_output_data()
    )
    return output, name, email, cur_addr, perm_addr
