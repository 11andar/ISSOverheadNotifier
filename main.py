from iss import ISS
import time
from location import Location
from notification import Notification
from data import my_data

# Initialize objects
iss = ISS()
notification = Notification(email=my_data["email"], password=my_data["app_password"])
location = Location(latitude=my_data["lat"], longitude=my_data["lng"])

# Define total execution time and interval for checking ISS position
total_exec_time = 60
interval = 10

# Record the start time of execution
start_exec_time = time.time()

# Loop to continuously monitor ISS position
while True:
    # Wait for the defined interval before next iteration
    time.sleep(interval)

    # Update ISS position to the current one
    iss.fetch_position()

    # Print ISS location data
    print(iss)

    # Show ISS position on map
    iss.show_position_on_map()

    # Check if ISS is above the specified location and observation is possible
    if iss.is_above(location) and location.is_observation_possible():
        notification.send_email(location)

    # Check if total execution time has elapsed
    if time.time() - start_exec_time >= total_exec_time:
        break
