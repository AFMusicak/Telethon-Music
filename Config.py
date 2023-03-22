import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23926880"))
    API_HASH = os.environ.get("API_HASH", "561db8bb43f5b153080b3cd2eca27516")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5854958317:AAHODB4syvt2hqMJHte_1iUB5GXxcFETalg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCeIabnxsx3RKwBjtYC_hcW8gjIOYUnkDVrF3_8Qw7MvyZiTaxEKwU_EWcSh3X6jJkD7sj2ou6384Iz2MPI4Gr7SYjyNfKW-LWBDhpsHDgQObITZnndYAZdwkKmXYL7ymaaIV0gMWchwvjhxWFGdkBnB6-vQ7UiMNx23vM-_OPS3N0WO8dqHKmeddwlvjAY5NuDHw3oGs37A-hbYaLGlekb_LTwEYhZD7V5xZNLgn7lSuh-wkbywwNBKyGKBoOFHHby_r9I-RE3Gjvn7d3OlSc4hPXkERYCPz5ygfwrfJSLsQrqeG3RrIxr9Up8UxNOGXfKG2PWIStkKf2gt6FA5vNoAAAAAVzguFEA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@afm_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5853198417")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
