import pytest

from pydantic import BaseModel


class _Profile(BaseModel):
    name: str
    age: int


class _User(BaseModel):
    profile: _Profile
    emails: list[str]


@pytest.fixture()
def user_01():
    return {
        "user": {
            "profile": {"name": "Alice", "age": 30},
            "settings": {"theme": "dark"},
            "emails": [
                "alice@gmail.com",
                "alice@hotmail.com",
            ],
        }
    }


@pytest.fixture()
def user_02():
    profile = _Profile(name="Alice", age=30)
    emails = ["alice@gmail.com", "alice@hotmail.com"]
    user = _User(profile=profile, emails=emails)
    return user


@pytest.fixture()
def user_03():
    return {
        "user": {
            "user.profiles": {  # Note dots
                "name": "Alice",
                "age": 30,
            },
            "user emails": [  # Note spaces
                "alice@gmail.com",
                "alice@hotmail.com",
            ],
        }
    }
