import requests
from datetime import datetime, timedelta
from data import my_data


class Location:
    """Class representing a geographical location and it's weather."""

    def __init__(self, latitude=0.0, longitude=0.0):
        """Initialize the Location object."""
        self.latitude = latitude
        self.longitude = longitude
        self.last_update_time = datetime.now()
        self.data = None
        self.update_data()
        self.name = self.data["name"] if self.data else None

    def __str__(self):
        """Return a string representation of the location."""
        return f"{self.name}: ({self.latitude}, {self.longitude})"

    def update_data(self):
        """Update location data using OpenWeather API."""
        open_weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"

        parameters = {
            "lat": self.latitude,
            "lon": self.longitude,
            "appid": my_data["OW_API_key"],
            "units": "metric"
        }

        # Get data from OpenWeather API
        response = requests.get(open_weather_endpoint, params=parameters)
        self.data = response.json()
        self.last_update_time = datetime.now()

    def is_data_outdated(self) -> bool:
        """Check if the location data is outdated."""
        if self.last_update_time is None:
            return True
        return datetime.now() - self.last_update_time > timedelta(hours=1)

    def is_dark(self) -> bool:
        """Check if it's dark"""
        if self.is_data_outdated():
            self.update_data()

        sunrise_timestamp = self.data["sys"]["sunrise"]
        sunset_timestamp = self.data["sys"]["sunset"]

        sunrise_time = str(datetime.utcfromtimestamp(sunrise_timestamp)).split(" ")[1]
        sunset_time = str(datetime.utcfromtimestamp(sunset_timestamp)).split(" ")[1]

        sunrise_hour = int(sunrise_time.split(":")[0])
        sunset_hour = int(sunset_time.split(":")[0])

        time_now = datetime.now()
        hour_now = time_now.hour

        if sunset_hour < hour_now < sunrise_hour:
            return True
        return False

    def sky_is_clear(self) -> bool:
        """Check if the sky is clear."""
        if self.is_data_outdated():
            self.update_data()

        cloudiness = self.data["clouds"]["all"]

        if cloudiness <= 30:
            return True
        return False

    def is_observation_possible(self) -> bool:
        """Check if observation of the sky is possible."""
        if self.is_data_outdated():
            self.update_data()

        if self.is_dark() and self.sky_is_clear():
            return True
        return False
