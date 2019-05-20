from datetime import datetime

from family import mock_now


def test_mock_now():
    now = datetime.now()
    with mock_now(1985, 7, 3):
        assert datetime.now() == datetime(1987, 7, 3)
    assert now == datetime.now()
