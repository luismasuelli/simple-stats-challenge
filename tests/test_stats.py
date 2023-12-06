import pytest
from simple_stats import Capture


def test_invalid_values():
    """
    Properly tests exceptions when adding invalid values.
    """

    capture = Capture()
    capture.add(0)
    capture.add(1)
    capture.add(2)
    capture.add(3)

    with pytest.raises(ValueError):
        capture.add(1.0)

    with pytest.raises(ValueError):
        capture.add("1")

    with pytest.raises(ValueError):
        capture.add(None)

    with pytest.raises(ValueError):
        capture.add(-1)

    with pytest.raises(ValueError):
        capture.add(1000)

    with pytest.raises(ValueError):
        capture.add(1001)

    with pytest.raises(ValueError):
        capture.add(100100)

    capture.add(999)
    capture.add(998)
    capture.add(997)
    capture.add(996)


def test_less():
    """
    Properly tests the less(x) method.
    """

    capture = Capture()
    capture.add(9)
    capture.add(3)
    capture.add(3)
    capture.add(3)
    capture.add(4)
    capture.add(4)
    capture.add(5)
    capture.add(8)
    capture.add(9)

    stats = capture.build_stats()

    assert stats.less(4) == 3
    assert stats.less(3) == 0
    assert stats.less(999) == 9
    assert stats.less(5) == 5
    assert stats.less(6) == 6
    assert stats.less(8) == 6
    assert stats.less(9) == 7
    assert stats.less(-100000) == 0


def test_greater():
    """
    Properly tests the greater(x) method.
    """

    capture = Capture()
    capture.add(999)
    capture.add(999)
    capture.add(998)
    capture.add(990)
    capture.add(989)
    capture.add(989)
    capture.add(988)
    capture.add(987)
    capture.add(985)

    stats = capture.build_stats()

    assert stats.greater(999) == 0
    assert stats.greater(1000) == 0
    assert stats.greater(100000) == 0
    assert stats.greater(998) == 2
    assert stats.greater(985) == 8
    assert stats.greater(984) == 9
    assert stats.greater(980) == 9
    assert stats.greater(0) == 9
    assert stats.greater(-100) == 9


def test_between():
    """
    Properly tests the between(x, y) method,
    including the "invalid arguments" exception.
    """

    capture = Capture()
    capture.add(9)
    capture.add(9)
    capture.add(10)
    capture.add(11)
    capture.add(11)
    capture.add(11)
    capture.add(12)
    capture.add(12)
    capture.add(13)
    capture.add(13)
    capture.add(13)
    capture.add(14)
    capture.add(15)

    stats = capture.build_stats()

    with pytest.raises(ValueError):
        assert stats.between(5, 4) == 0

    assert stats.between(10, 10) == 1
    assert stats.between(11, 11) == 3
    assert stats.between(8, 8) == 0
    assert stats.between(-80000, 8) == 0
    assert stats.between(15, 15) == 1
    assert stats.between(16, 16) == 0
    assert stats.between(16, 1600000) == 0
    assert stats.between(-1000000000, 11) == 6
    assert stats.between(-1000000000, 11000000000) == 13
    assert stats.between(-1000000000, -4) == 0
    assert stats.between(100, 100000000) == 0
    assert stats.between(12, 1000) == 7
    assert stats.between(12, 100000000) == 7
    assert stats.between(10, 13) == 9
    assert stats.between(12, 14) == 6
