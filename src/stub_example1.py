# Stub objects are used when you need to provide predefined responses to
# method calls or attribute access.
import sys
import unittest.mock

import pytest


class WeatherService:
    def get_temperature(self, location) -> int:
        # External API call to fetch the temperature for the given location
        pass


class TripPlanner:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def plan_trip(self, location):
        """
        Plan a trip based on the temperature of the given location.
        """
        temperature = self.weather_service.get_temperature(location)
        return 18 <= temperature <= 26


# Mock way we did
@pytest.mark.parametrize(
    "temperature, expected",
    [
        (20, True),
        (10, False),
        (30, False),
    ],
)
def test_plan_trip_mock(temperature, expected):
    weather_service = unittest.mock.Mock()
    weather_service.get_temperature.return_value = temperature
    trip_planner = TripPlanner(weather_service)
    assert trip_planner.plan_trip("London") is expected


# Stub way we can have
class StubWeatherService:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self, location):
        # We are returning a fixed value for the temperature here
        return self.temperature


@pytest.mark.parametrize(
    "temperature, expected",
    [
        (20, True),
        (10, False),
        (30, False),
    ],
)
def test_plan_trip_stub(temperature, expected):
    weather_service = StubWeatherService(temperature)
    trip_planner = TripPlanner(weather_service)
    assert trip_planner.plan_trip("Dummy City!") is expected


if __name__ == "__main__":
    sys.exit(pytest.main(["-vv"]))
