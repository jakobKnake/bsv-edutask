import pytest
import unittest.mock as mock

from src.util.helpers import ValidationHelper

@pytest.fixture
def user(age: int):
    mockedusercontroller = mock.MagicMock()
    mockedusercontroller.get.return_value = {'age': age}
    mocked = ValidationHelper(usercontroller=mockedusercontroller)
    return mocked

testage = [
    (-1, 'invalid'),
    (0, 'underaged'),
    (2, 'underaged'),
    (17, 'underaged'),
    (18, 'underaged'), # Should be valid but functions says over 18
    (25, 'valid'),
    (120, 'valid'),
    (121, 'invalid')
]
@pytest.mark.unit
@pytest.mark.parametrize('age, expected', testage)
def test_validateAge_valid(user, expected):
    res = user.validateAge(userid=None)
    print(res)
    assert res == expected

