from enum import Enum

class Notifications(Enum):
    """
    Represents notification messages used in the project.
    """
    LOGIN_SUCCESS = "You logged into a secure area!"
    REGISTRATION_SUCCESS = "Successfully registered, you can log in now."
    MESSAGE_SENT_SUCCESS = "Message was sent successfully"