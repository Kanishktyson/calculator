import pytest

from calculator import evaluate, parse


# ── evaluate ──────────────────────────────────────────────

@pytest.mark.parametrize("a,op,b,expected", [
    (2, "+", 3, 5.0),
    (10, "-", 4, 6.0),
    (6, "*", 7, 42.0),
    (7, "/", 2, 3.5),
    (10, "%", 3, 1.0),
    (2, "**", 10, 1024.0),
])
def test_evaluate_basic(a, op, b, expected):
    assert evaluate(a, op, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate(1, "/", 0)


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate(1, "%", 0)


def test_unknown_operator():
    with pytest.raises(ValueError):
        evaluate(1, "&", 2)


# ── parse ─────────────────────────────────────────────────

def test_parse_valid():
    assert parse("2 + 3") == (2.0, "+", 3.0)
    assert parse("  10   **  2 ") == (10.0, "**", 2.0)


@pytest.mark.parametrize("bad", ["2 +", "2 3", "a + b", "2 + 3 + 4", ""])
def test_parse_invalid(bad):
    with pytest.raises(ValueError):
        parse(bad)
