import socket
import sys

import pytest

try:
    from src import main

except ModuleNotFoundError:
    sys.path.append("..")
    from src import main

def test_get_coord_from_city():
    # Test to ensure the coorindates are returned correctly
    zip_code = '98103'
    coords = '47.67368145749622,-122.34398167484034'

    value, location = main.get_coords_from_city(zip_code)

    assert value == coords

def test_get_coord_exception():
    # Test to ensure the coordinates function raises an error for
    # invalid entries
    with pytest.raises(ValueError):
        val = main.get_coords_from_city("invalidname")


def test_get_forecast():
    # Test to ensure the forecast data list returns 7 days of weather
    zip_code = '98103'
    coords, location = main.get_coords_from_city(zip_code)

    forecast_data = main.get_forecast(coords)

    assert len(forecast_data) > 0
