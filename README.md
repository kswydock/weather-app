## weather-app

### Overview
This is a proof-of-concept weather application.

I created this to use a geographic location package for python called
`geocoder` to allow a user to input a location and the national weather
service API would be used to gather weather information for them.

I then used `plotly` to take that data and plot it visually for the user.

### Future Capability

I could potentially utilize Heroku to deploy this app to a server and have it run
off of a basic `flask` application to pull information. The application would
be very basic in that it would have an input field for the user to enter location data
and then there would be calls to the python functions to find and display the data.

A user could choose to display it via text or graphically via `plotly` charts rendered
for the user.