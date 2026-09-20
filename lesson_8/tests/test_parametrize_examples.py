"""
Варианты параметризации pytest (теория / демо без браузера).

Покрыто:
1) @parametrize + ids
2) pytest.param + marks (xfail/skip)
3) несколько @parametrize (декартово произведение)
4) fixture(params=...)
5) indirect=True
6) pytest_generate_tests / metafunc
7) данные из dict / csv-like списка
"""

import csv
from pathlib import Path

import pytest


# --- 1. классический parametrize + ids ---
@pytest.mark.unit
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (10, -3, 7), (0, 0, 0)],
    ids=["1+2", "10-3", "zeros"],
)
def test_parametrize_ids(a, b, expected):
    assert a + b == expected


# --- 2. pytest.param с marks ---
@pytest.mark.unit
@pytest.mark.parametrize(
    "expr, expected",
    [
        ("2+2", 4),
        pytest.param("6*9", 42, marks=pytest.mark.xfail(reason="не 42, а 54"), id="xfail-hitchhiker"),
        pytest.param("1/0", None, marks=pytest.mark.skip(reason="демо skip через param"), id="skip-div0"),
    ],
)
def test_param_with_marks(expr, expected):
    assert eval(expr) == expected


# --- 3. несколько декораторов = cartesian product ---
@pytest.mark.unit
@pytest.mark.parametrize("x", [1, 2], ids=["x1", "x2"])
@pytest.mark.parametrize("y", [10, 20], ids=["y10", "y20"])
def test_cartesian(x, y):
    assert x * y in {10, 20, 40}


# --- 4. параметризация фикстуры ---
@pytest.fixture(params=["chrome", "firefox"], ids=["br-chrome", "br-firefox"])
def fake_browser(request):
    return request.param


@pytest.mark.unit
def test_fixture_params(fake_browser):
    assert fake_browser in {"chrome", "firefox"}


# --- 5. indirect: параметр уходит в фикстуру ---
@pytest.fixture
def sized_box(request):
    width, height = request.param
    return {"w": width, "h": height, "area": width * height}


@pytest.mark.unit
@pytest.mark.parametrize(
    "sized_box",
    [(1920, 1080), (390, 844)],
    ids=["desktop", "mobile"],
    indirect=True,
)
def test_indirect_viewport(sized_box):
    assert sized_box["area"] == sized_box["w"] * sized_box["h"]
    if sized_box["w"] < 600:
        assert sized_box["h"] > sized_box["w"]


# --- 6. pytest_generate_tests ---
def pytest_generate_tests(metafunc):
    if "generated_n" in metafunc.fixturenames:
        metafunc.parametrize("generated_n", [2, 4, 8], ids=["n2", "n4", "n8"])


@pytest.mark.unit
def test_generate_tests(generated_n):
    assert generated_n % 2 == 0


# --- 7. данные из «таблицы» / csv ---
CASES = [
    {"login": "user1", "ok": True},
    {"login": "bad", "ok": False},
]


@pytest.mark.unit
@pytest.mark.parametrize("case", CASES, ids=[c["login"] for c in CASES])
def test_dict_cases(case):
    assert isinstance(case["ok"], bool)


@pytest.mark.unit
def test_csv_like(tmp_path):
    path = tmp_path / "data.csv"
    path.write_text("a,b,sum\n1,2,3\n4,5,9\n", encoding="utf-8")
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    for row in rows:
        assert int(row["a"]) + int(row["b"]) == int(row["sum"])


@pytest.mark.unit
def test_path_exists():
    assert Path(__file__).exists()
