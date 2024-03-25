import requests
import folium
from location import Location


class ISS:
    """Class representing the International Space Station (ISS)."""

    def __init__(self):
        """Initialize the ISS object."""
        self._latitude = None
        self._longitude = None
        self.fetch_position()

    def __str__(self):
        """Return a string representation of the ISS position."""
        return f"ISS position: (latitude: {self._latitude}, longitude: {self._longitude})"

    def fetch_position(self):
        """Fetch the current position of the ISS."""
        # Get data from ISS API
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        # Set ISS latitude and longitude
        self._latitude = float(data["iss_position"]["latitude"])
        self._longitude = float(data["iss_position"]["longitude"])

    def is_above(self, location: Location) -> bool:
        """Check if the ISS is above the specified location."""
        # Define the distance threshold for ISS visibility
        distance = 5

        # Check if ISS's latitude and longitude are within the desired range from the location
        latitude_check = location.latitude - distance < self._latitude < location.latitude + distance
        longitude_check = location.longitude - distance < self._longitude < location.longitude + distance

        # Return True if ISS is within range, False otherwise
        return latitude_check and longitude_check

    def show_position_on_map(self):
        """Display the current ISS position on a map."""
        # Create a map centered at the ISS coordinates
        iss_on_map = folium.Map(location=[self._latitude, self._longitude], zoom_start=2)

        # Add a marker at the ISS coordinates
        folium.Marker([self._latitude, self._longitude], popup="ISS position").add_to(iss_on_map)

        # Save the map as an HTML file
        iss_on_map.save("iss_on_map.html")
