from .component import one
from .component import two


def test_one():
    assert one() == "hello"


def test_two():
    assert two(False) == "world"


def test_two2():
    assert two(True) == "world"
