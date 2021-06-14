from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "AQBvV11x81WFr6s7oo_171NmUcfkRhcNw3g7uiduKarkLuvojDcyr3XAQIIpr5sJ4-Hmj4T7GWTABwGBpkq6mcnpF-1KmkajcbReETW-cX9ZdT6aoNzGg4cR7cw4T5gbSRXij-zHd7C6XOqyQO7HzXQ9VITktu6-MjLDWSdDpb9w1ibJNducIUXK9_nU8hCgC5kAmPSy1CHqJnNAPzXxgUEshMPpwjASdy-BLSXz1OIMhIYEgaOyKDtZl7EtL6kjFG90kWqS2JwVe8rpBB4gkDviZK_56IzRjJHq0RuPggPBM5cLbqJ0en54-eSK0t2a2BOO8FLCGztgZAYoaOsl0Pd1L7y8qgA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAG_qNWSYnl1jEUvAnhaqLrXUFONUKObIJM")
BOT_NAME = getenv("BOT_NAME", "patriciaXmusic")

API_ID = int(getenv("API_ID", "3088812"))
API_HASH = getenv("API_HASH", "d51f13802ef40ccb115e333a5f9dc9e7")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1801516703").split()))
