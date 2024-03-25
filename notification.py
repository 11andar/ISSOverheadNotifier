import smtplib
from data import RECIPIENTS
from location import Location


class Notification:
    """Class responsible for sending email notifications."""

    def __init__(self, email: str, password: str):
        """Initialize the Notification object with email credentials."""
        self._email = email
        self._password = password

    def send_email(self, location: Location):
        """Send email notifications to recipients."""
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                # Secure connection
                connection.starttls()
                connection.login(user=self._email, password=self._password)

                for recipient in RECIPIENTS:
                    # Construct the email message
                    subject = "ISS Tracker"
                    body = (f"Hi {recipient},\n\nISS is approximately somewhere above {location.name}. "
                            f"Look up and see if you can spot it! 🛰️")
                    message = f"Subject:{subject}\n\n{body}"

                    # Encode the message using UTF-8
                    message_utf8 = message.encode("utf-8")

                    # Send the email
                    connection.sendmail(from_addr=self._email,
                                        to_addrs=RECIPIENTS[recipient]["email"],
                                        msg=message_utf8)

        except smtplib.SMTPException as error:
            print(f"Error: {error}")
