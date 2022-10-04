import pytest
import looping
def test_looper_initialization():
    lpr = looping.LoopingVariable(10)
    assert lpr.value == 0


@pytest.mark.parametrize("inc,bound", [
    (1, 2),
    (1, 3),
    (2, 3),
    (5, 10)
])
def test_looper_increase_without_looping(inc, bound):
    lpr = looping.LoopingVariable(bound)
    lpr.increase(inc)
    assert lpr.value == inc


@pytest.mark.parametrize("bound", [
    1, 2, 3, 4, 5
])
def test_looper_increase_to_bound(bound):
    lpr = looping.LoopingVariable(bound)
    lpr.increase(bound)
    assert lpr.value == 0


@pytest.mark.parametrize("inc,bound,expected", [
    (3, 2, 1),
    (4, 3, 1),
    (5, 3, 2),
    (15, 10, 5),
    (16, 10, 6),
    (17, 10, 7),
    (18, 10, 8),
    (19, 10, 9),
])
def test_looper_increase_past_bound(inc, bound, expected):
    lpr = looping.LoopingVariable(bound)
    lpr.increase(inc)
    assert lpr.value == expected


@pytest.mark.parametrize("inc,bound,expected", [
    (20, 10, 0),
    (31, 10, 1),
    (42, 10, 2),
])
def test_looper_increase_twice_past_bound(inc, bound, expected):
    lpr = looping.LoopingVariable(bound)
    lpr.increase(inc)
    assert lpr.value == expected