import os

import automation_practice_form_po


class AutomationPracticeFormTestSuite:
    URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    def setup(self):
        self.form = automation_practice_form_po.AutomationPracticeFormPO(self.URL)
        self.form.setup()
        self.tmp_file_name = self._create_tmp_file()

    def _create_tmp_file(self):
        file_path = os.path.abspath("test_file.jpg")
        with open(file_path, "w") as file:
            file.write("Test")
        return file_path

    def tear_down(self):
        if hasattr(self, "tmp_file_name") and os.path.exists(self.tmp_file_name):
            os.remove(self.tmp_file_name)
        if hasattr(self, "form"):
            self.form.tear_down()

    def run_case(self, **data):
        # setup/tear_down на каждый тест
        self.setup()
        try:
            self.form.fill_in_form(self.tmp_file_name, **data)
            self.form.assert_form(self.tmp_file_name, **data)
        finally:
            self.tear_down()

    def test_form_positive01(self):
        self.run_case(
            first_name="Dmitry",
            last_name="Bugaev",
            email="bugaev@example.com",
            gender="Male",
            user_number="1234567890",
            birth_day=("1988", "4", "22"),
            subjects=("Maths", "English"),
            hobbies=("Sports", "Music"),
            current_address="г. Санкт-Петербург, ул. Невский проспект, д 101",
            state="NCR",
            city="Noida",
        )

    def test_form_positive02(self):
        self.run_case(
            first_name="Anna",
            last_name="Smirnova",
            email="anna.smirnova@mail.ru",
            gender="Female",
            user_number="9001112233",
            birth_day=("1995", "11", "15"),
            subjects=("Computer Science",),
            hobbies=("Reading",),
            current_address="Москва, Тверская 1",
            state="NCR",
            city="Delhi",
        )

    def test_form_positive03(self):
        self.run_case(
            first_name="Alex",
            last_name="Other",
            email="alex.other@test.com",
            gender="Other",
            user_number="9112223344",
            birth_day=("2000", "0", "05"),
            subjects=("Physics", "Chemistry"),
            hobbies=("Sports", "Reading", "Music"),
            current_address="Казань, Баумана 5",
            state="Haryana",
            city="Karnal",
        )


if __name__ == "__main__":
    suite = AutomationPracticeFormTestSuite()
    suite.test_form_positive01()
    suite.test_form_positive02()
    suite.test_form_positive03()
    print("OK: automation practice form suite")
