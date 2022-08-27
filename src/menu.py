import sys

import main


def current_temp_by_city():
    print("Required Format: City, State or a zip code")
    city = input("Enter a city/state combinatation or zip code: ")
    weather_coords, location = main.get_coords_from_city(city)
    temp = main.get_current_temp(weather_coords)

    print("-----------")
    print(f"Current temperature in {location} is: {temp}F\n")


def forecast_by_city():
    print("Required Format: City, State or a zip code")
    city = input("Enter a city/state combinatation or zip code: ")

    weather_coords, location = main.get_coords_from_city(city)
    forecast = main.get_forecast(weather_coords)

    print(f"The 7 day forecast for {location} starting tomorrow is as follows:\n")
    print("-------------")
    for val in forecast:
        date = val["startTime"][:10]
        print(f"{val['name']} - {date}: High Temp of {val['temperature']}")


def plotted_forecast():
    print("Required Format: City, State or a zip code")
    city = input("Enter a city/state combinatation or zip code: ")

    weather_coords, location = main.get_coords_from_city(city)
    forecast = main.get_forecast(weather_coords)

    main.plot_forecast(forecast, location)


def quit_program():
    sys.exit()


if __name__ == "__main__":
    menu_options = {
        "A": current_temp_by_city,
        "B": forecast_by_city,
        "C": plotted_forecast,
        "Q": quit_program,
    }

    while True:
        user_selection = input(
            """
                               A: Current Temp by City
                               B: Forecast by City
                               C: Plotted future forecast by City
                               Q: Quit Program

                               Please enter a choice: """
        )
        try:
            input_val = user_selection.strip().upper()
            if input_val in menu_options:
                menu_options[input_val]()
            else:
                print("Invalid option. Please try again.")
        except ValueError as err:
            print("\nLOCATION ERROR: Please see below:")
            print(err)
        except KeyError as err:
            print("\nERROR: Please see below:")
            print(err)
