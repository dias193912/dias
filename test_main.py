from main import multiply


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 3) == -3
    assert multiply(0, 10) == 0
