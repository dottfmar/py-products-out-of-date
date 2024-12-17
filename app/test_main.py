import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "mocked,expected",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 1, 30), []),
        (datetime.date(2022, 3, 2), ["salmon", "chicken", "duck"]),
        (datetime.date(2022, 2, 10), ["chicken", "duck"])
    ]
)
def test_should_return_correct_list_of_outdated_products(
        mocked: datetime.date,
        expected: list[str]
) -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 8),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    with mock.patch("datetime.date") as mock_date:
        mock_date.today.return_value = mocked
        assert outdated_products(products) == expected
