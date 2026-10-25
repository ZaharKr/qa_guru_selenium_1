import unittest


def normalize_email(value: str) -> str:
    return value.strip().lower()


def short_body(body: str, size: int = 10) -> str:
    return body[:size] + "..."


class TestEmailUtils(unittest.TestCase):
    def test_normalize_email(self):
        self.assertEqual(normalize_email(" Alice@Mail.RU "), "alice@mail.ru")

    def test_short_body(self):
        self.assertEqual(short_body("Hello World!!!"), "Hello Worl...")

    def test_short_body_custom_size(self):
        self.assertEqual(short_body("abcdef", 3), "abc...")


if __name__ == "__main__":
    unittest.main()
