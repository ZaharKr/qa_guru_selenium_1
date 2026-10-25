import json
import logging
import sys
import allure
import pytest
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@allure.epic("Веб-приложение")
@allure.feature("Авторизация")
class TestAuth:

    @allure.story("Успешный вход в систему")
    @allure.title("Корректный логин и пароль")
    @allure.description("Some test description")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("https://bsu.by", "Ссылка на тест-кейс")
    def test_successful_login(self):
        with allure.step("Открытие страницы логина"):
            time.sleep(0.5)
        with allure.step("Ввод валидных данных"):
            time.sleep(0.5)
        with allure.step("Нажатие кнопки Вход"):
            time.sleep(0.5)
        with allure.step("Описание проверки в терминах бизнеса"):
            assert True

    @allure.story("Негативные сценарии")
    @allure.title("Неверный пароль")
    @allure.issue("https://bsu.by", "Баг-трекер №123")
    @allure.severity(allure.severity_level.NORMAL)
    def test_wrong_password(self):
        with allure.step("Ввод неверного пароля"):
            allure.attach("Неверный логин или пароль", name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            assert False, "Система не должна пропускать пользователя"

@allure.step("Открываем главную страницу")
def open_main_page():
    time.sleep(0.5)
    pass

@allure.epic("Вспомогательные функции")
@allure.feature("Калькулятор оценок")
class TestCalculator:

    @allure.story("Параметризованные тесты")
    @pytest.mark.parametrize("a, b, expected", [(2, 2, 4), (5, 5, 10), (3, 4, 7)])
    def test_math_addition(self, a, b, expected):
        with allure.step(f"Сложение {a} и {b}"):
            time.sleep(0.5)
            result = a + b
        with allure.step(f"Проверка: {result} равно {expected}"):
            time.sleep(0.5)
            assert result == expected

    @allure.story("Прикрепление файлов и логов")
    def test_attach_file(self):
        time.sleep(0.5)
        allure.attach("Text content", name="Text", attachment_type=allure.attachment_type.TEXT)

        allure.attach("<xml><body>Тестовый ответ API</body></xml>", name="API Response", attachment_type=allure.attachment_type.XML)

        allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=allure.attachment_type.HTML)

        user_data = {"name": "Alice", "age": 30, "is_admin": False} # Python dictionary
        allure.attach(json.dumps(user_data), name="Json", attachment_type=allure.attachment_type.JSON)
        assert True

    @allure.story("Пропуск тестов")
    @pytest.mark.skip(reason="Функциональность находится в разработке")
    def test_feature_in_progress(self):
        time.sleep(0.5)
        open_main_page()
        assert True

def test_no_labels():
    time.sleep(0.5)
    assert True

# Первый способ
def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(allure.severity_level.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.description("Some updated dynamic test description")
    allure.dynamic.link("https://github.com", name="Testing")
    time.sleep(0.5)
    assert True

# Второй способ
@allure.tag("web")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Ivanov")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    time.sleep(0.5)
    assert True

@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123", name="Issue Tracker")
@allure.testcase("TMS-456", name="Test Case")
def test_link():
    assert True

def test_dynamic_link():
    allure.dynamic.link("https://example.com", name="Dynamic Docs")
    assert True

# Плагин allure-pytest автоматически перехватывает потоки:
# - stdout (print)
# - stderr
# - стандартный модуль logging (logger.info)
# прикрепляя их в виде файлов к каждому тесту в отчете Allure Report.
# В интерфейсе Allure внутри карточки выполненного теста в блоках stdout, stderr и log отобразится вся информация, перехваченная из кода.
def test_allure_logs_example():
    # 1. Запись в стандартный лог (логгирование)
    logger.info("Это сообщение уровня INFO через стандартный модуль logging")
    logger.warning("Это предупреждение (WARNING) для отчета")
    
    # 2. Вывод в stdout (функция print)
    print("Текст, выведенный в стандартный поток вывода stdout")
    
    # 3. Вывод в stderr (ошибки в консоль)
    print("Текст, отправленный в поток ошибок stderr", file=sys.stderr)
    
    # 4. Ручное добавление вложений через Allure (опционально)
    allure.attach("Дополнительные данные", name="Custom Text Attachment", attachment_type=allure.attachment_type.TEXT)
    
    assert True

def test_open_dynamic_url():
    current_url = "https://example.com"
    
    # Добавление динамического параметра в таблицу параметров теста
    allure.dynamic.parameter("Target URL", current_url)
    
    # Добавление динамической ссылки в блок Links отчета
    allure.dynamic.link(current_url, name="Opened Page")
    
    assert "example.com" in current_url

# Фабрики фикстур в pytest — это шаблон проектирования, где фикстура возвращает функцию-помощник (замыкание), а не готовое статичное значение.
# Это позволяет динамически создавать объекты с разным состоянием прямо внутри теста.

# Замыкание — это внутренняя функция, которая помнит переменные из своей внешней области видимости.
# В фабриках фикстур замыкание захватывает контекст фикстуры (например, подключение к БД или хранилище созданных сущностей),
# позволяя управлять жизненным циклом и накапливать состояние (например, список созданных объектов для последующей автоочистки).

# Главные преимущества паттерна:
# Гибкость: можно создавать нужное количество объектов в рамках одного теста.
# Инкапсуляция: логика создания и очистки скрыта внутри одной фикстуры.
# Контроль: состояние (списки созданных сущностей) очищается автоматически через yield.

@pytest.fixture
def make_user():
    # Состояние: список для отслеживания созданных пользователей
    created_users = [] # имитация БД

    # Замыкание (фабрика)
    def _user_factory(name: str, role: str = "user"):
        user = {"id": len(created_users) + 1, "name": name, "role": role}
        created_users.append(user) # Здесь код добавления пользователя в базу данных
        return user

    yield _user_factory

    # Управление состоянием: автоматическая очистка после теста
    for user in created_users:
        print(f"Удаление пользователя в БД: {user['name']}")
        # Здесь код удаления из базы данных

def test_admin_and_guest(make_user):
    # Динамическое создание объектов с разным состоянием
    admin = make_user("Иван", role="admin")
    guest = make_user("Анна", role="guest")

    assert admin["role"] == "admin"
    assert guest["role"] == "guest"

# pip install -r requirements.txt
# pytest .\test_allure_features.py
# allure serve .\allure-results\
