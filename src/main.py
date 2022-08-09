import calendar
import typing

import geocoder
import pandas as pd
import plotly.express as px
import requests

"""
This python package is designed to utilize the national weather service
API to provide weather information. Additional funcitonality
will be added to display the weather as well.
"""
API_ADDRESS = "https://api.weather.gov/points/"


def get_coords_from_city(city_name: str) -> str:
    # Function to get coordinates from city name or zip code
    g = geocoder.osm(city_name)
    lat_long = g.latlng
    location = g.address
    if lat_long is None:
        raise ValueError("Location could not be found. Please try again.")

    if g.country_code != "us":
        raise ValueError(
            "Location found is outside of US. Please try a different format."
        )

    coord_string = f"{lat_long[0]},{lat_long[1]}"

    return coord_string, location


def get_current_temp(coord_string: str) -> int:
    # Function to get weather by city name.
    # `Input:` City as string i.e. "Mountain View, CA"
    # `Output:` dict of weather info`
    api_string = API_ADDRESS + coord_string

    req_1 = requests.get(api_string).json()
    forecast_url = req_1["properties"]["forecastHourly"]

    forecast = requests.get(forecast_url).json()
    forecast_dict = forecast["properties"]["periods"]
    current_temp = forecast_dict[00]["temperature"]

    return current_temp


def get_forecast(coord_string: str) -> list:
    # Function to get forecast for a specific location
    api_string = API_ADDRESS + coord_string
    forecast_list = []
    req_1 = requests.get(api_string).json()
    forecast_url = req_1["properties"]["forecast"]
    forecast = requests.get(forecast_url).json()
    forecast_dict = forecast["properties"]["periods"]
    day_list = tuple(calendar.day_name)

    forecast_list.append(forecast_dict[0])

    for forecast_data in forecast_dict:
        day_name = forecast_data["name"]
        exist_count = day_list.count(day_name)

        if exist_count > 0:
            forecast_list.append(forecast_data)
        else:
            continue

    return forecast_list


def plot_forecast(forecast_data: list, location_name: str) -> None:
    # Function to plot the forecast data in an interactive window
    yaxes_range = [0, 105]
    date_range = [
        forecast_data[0]["startTime"][:10],
        forecast_data[-1]["startTime"][:10],
    ]
    df = pd.DataFrame(forecast_data)
    fig = px.bar(
        df,
        x="name",
        y="temperature",
        hover_data=["detailedForecast"],
        color="temperature",
        color_continuous_scale=["blue", "yellow", "red"],
        range_color=yaxes_range,
    )

    fig.update_yaxes(range=yaxes_range, fixedrange=True)
    fig.update_xaxes(fixedrange=True)
    fig.update_layout(
        title=f"Weather forecast for {location_name} from {date_range[0]} to {date_range[1]}",
        xaxis_title="Day of the Week",
        yaxis_title="Temperature (F)",
    )
    fig.show()
