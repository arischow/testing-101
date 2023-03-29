# Dummy objects are used when you need to pass an argument to satisfy
# the signature of a function or a constructor, but the actual value of the argument
# is not used in the test.

import sys
import pytest


class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @property
    def is_adult(self):
        return self.age >= 18


class TestUser:
    # Dummy values won't be used in this test
    dummy_name = "Dummy Aris"
    dummy_address = "Milky Way"

    def test_is_adult(self):
        user = User(self.dummy_name, 30, self.dummy_address)
        assert user.is_adult

    def test_is_not_adult(self):
        user = User(self.dummy_name, 17, self.dummy_address)
        assert not user.is_adult


if __name__ == "__main__":
    sys.exit(pytest.main(["-vv"]))
