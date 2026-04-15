import pytest
from unittest.mock import patch

from src.util.dao import DAO
from src.util.validators import getValidator


@pytest.fixture
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
def daoObj():
    dao = DAO("testuser")
    return dao