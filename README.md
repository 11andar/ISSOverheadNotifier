# ISStracker

ISStracker is a Python repository designed for real-time tracking of the International Space Station (ISS). It offers functionalities to fetch ISS position data, determine its visibility from a specified location, visualize its position on a map, and send email notifications to recipients.

# Key Features:

# 1. ISS Position Tracking: 
Utilizes the Open Notify API to fetch the current latitude and longitude coordinates of the ISS.

# 2. Location-based Observation: 
Determines if the ISS is above a specified location and checks for optimal observation conditions. Additionally, integrates the OpenWeather API to retrieve weather data for the specified location.

# 3. Map Visualization: 
Displays the current position of the ISS on an interactive map using the Folium library.

# 4. Email Notifications: 
Sends email notifications to recipients, informing them about the ISS's approximate location and encouraging observation.

# Usage

To use ISStracker, follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages.
3. Sign in/up to OpenWeather here: https://home.openweathermap.org/users/sign_in.
4. Get your OpenWeather API key here: https://home.openweathermap.org/api_keys.
5. Enable 2-step verification on your Google account. 
6. Create app password on your Google account: Settings -> Security -> 
   2-Step Verification -> (scroll down) App passwords
7. Update the necessary configuration variables in 'data.py' file.
8. Run 'main.py'.
9. Open 'iss_on_map.html' using browser to see ISS's position on map.