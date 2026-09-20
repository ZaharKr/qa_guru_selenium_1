"""Unit-тесты без браузера: DI, моки, monkeypatch, approx, raises, tmp_path, caplog."""

import logging
from unittest.mock import Mock

import pytest

from di_example import ResourceManager


@pytest.mark.unit
def test_di_with_mock_connection():
    # Dependency Injection + mocking: подставляем fake connection
    fake = Mock()
    manager = ResourceManager(connection=fake)
    assert manager.update() is True
    fake.connect.assert_called_once()
    fake.update_database.assert_called_once()


@pytest.mark.unit
def test_di_set_connection_later():
    manager = ResourceManager()
    fake = Mock()
    manager.set_db_connection(fake)
    manager.update()
    fake.connect.assert_called_once()


@pytest.mark.unit
def test_raises_without_connection():
    manager = ResourceManager(connection=None)
    with pytest.raises(AttributeError):
        manager.update()


@pytest.mark.unit
def test_monkeypatch_env(monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")
    import os

    assert os.environ["APP_ENV"] == "test"


@pytest.mark.unit
def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)


@pytest.mark.unit
def test_tmp_path_write(tmp_path):
    report = tmp_path / "report.txt"
    report.write_text("pytest ok", encoding="utf-8")
    assert report.read_text(encoding="utf-8") == "pytest ok"


@pytest.mark.unit
def test_caplog_messages(caplog):
    logger = logging.getLogger("lesson7.demo")
    with caplog.at_level(logging.INFO):
        logger.info("hello from unit")
    assert "hello from unit" in caplog.text


@pytest.mark.unit
@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (10, -3, 7)], ids=["1+2", "10-3"])
def test_parametrize_pure(a, b, expected):
    assert a + b == expected


@pytest.mark.unit
def test_capsys(capsys):
    print("printed")
    captured = capsys.readouterr()
    assert "printed" in captured.out
