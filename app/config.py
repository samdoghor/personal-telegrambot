# imports
from dotenv import load_dotenv
import os

#load environment vairables from .env
load_dotenv()
apiKey=os.getenv('api_key')

# Enable debug mode.
DEBUG = True