import pytest
from src.util.helpers import hasAttribute

@pytest.fixture
def obj():
    return {"name": "Jane Doe"}

@pytest.mark.unit
def test_hasAttribute_True(obj):
    print("hejaa")
    res = hasAttribute(obj, "name")
    # print(res)
    assert res == True


@pytest.mark.unit
def test_hasAttribute_False(obj):
    print("hejaa")
    res = hasAttribute(obj, "age")
    # print(res)
    assert res == False


# @pytest.mark.unit
# def test_hasAttribute_None():
#    print("hejaa")
#    res = hasAttribute({None: "Jane"}, "name")
    # print(res)
#    assert res == False
