import pytest
from unittest.mock import patch

from src.util.dao import DAO
from src.util.validators import getValidator
from pymongo.errors import WriteError, DuplicateKeyError


@pytest.fixture
# Pre define a 'jsonfile' for validation
def jsonFile():
    return {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["firstName", "email"],
            "properties": {
                "firstName": {
                    "bsonType": "string",
                    "description": "the first name of a user must be determined"
                }, 
                "lastName": {
                    "bsonType": "string",
                },
                "email": {
                    "bsonType": "string",
                    "description": "the email address of a user must be determined",
                    "uniqueItems": True
                },
            }
        }
    }

@pytest.fixture
# DAO object, mocking the getValidator in __init__ with patch using the fixture above
def daoObj(jsonFile):
    patcher = patch('src.util.dao.getValidator', return_value=jsonFile)
    patcher.start()
    dao = DAO("testuser")
    
    yield dao
    patcher.stop()
    dao.collection.drop()

@pytest.mark.integration
def test_create_valid_data(daoObj):

    # Arrange
    data = {
        'firstName': 'Jakob',
        'email': 'jakob@hotmail.com',
        'lastName': 'Efternamn'
    }

    # Act
    res = daoObj.create(data)

    # Assert
    assert res is not None
    assert res['_id'] is not None
    assert res['firstName'] == 'Jakob'
    assert res['lastName'] == 'Efternamn'

@pytest.mark.integration
def test_create_invalid_firstname(daoObj):

    # Arrange
    data = {
        'firstName': 1234,
        'email': 'jakob@hotmail.com',
        'lastName': 'Efternamn'
    }

    # Act/Assert
    with pytest.raises(WriteError):
        daoObj.create(data)


@pytest.mark.integration
def test_create_invalid_email(daoObj):

    # Arrange
    data = {
        'firstName': 'Jakob',
        'email': 123,
        'lastName': 'Efternamn'
    }

    # Act/Assert
    with pytest.raises(WriteError):
        daoObj.create(data)

@pytest.mark.integration
def test_create_invalid_lastname(daoObj):

    # Arrange
    data = {
        'firstName': 'Jakob',
        'email': 'jakob@hotmail.com',
        'lastName': 123
    }

    # Act/Assert
    with pytest.raises(WriteError):
        daoObj.create(data)

@pytest.mark.integration
def test_create_no_firstname(daoObj):

    # Arrange
    data = {
        'email': 'jakob@hotmail.com',
        'lastName': 'Efternamn'
    }

    # Act/Assert
    with pytest.raises(WriteError):
        daoObj.create(data)

@pytest.mark.integration
def test_create_no_email(daoObj):

    # Arrange
    data = {
        'firstName': 'Jakob',
        'lastName': 'Efternamn'
    }

    # Act/Assert
    with pytest.raises(WriteError):
        daoObj.create(data)

@pytest.mark.integration
def test_create_email_notUnique(daoObj):

    # Arrange
    data1 = {
        'firstName': 'Jakob',
        'email': 'jakob@hotmail.com',
        'lastName': 'Efternamn'
    }

    data2 = {
        'firstName': 'Jakob',
        'email': 'jakob@hotmail.com',
        'lastName': 'Annan'
    }

    # Act
    # Create the first user
    daoObj.create(data1)

    # Act/Assert
    with pytest.raises(DuplicateKeyError):
        daoObj.create(data2)