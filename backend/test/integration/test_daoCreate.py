import pytest
from unittest.mock import patch

from src.util.dao import DAO
from src.util.validators import getValidator


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
    patcher.stop()
    return dao

