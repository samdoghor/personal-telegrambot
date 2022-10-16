# imports
import os

from dotenv import load_dotenv

# load environment vairables from .env
load_dotenv()

# configurations
apiKey=os.getenv('api_key')

dbName = os.getenv('db_name')
dbUsername = os.getenv ('db_username')
dbPassword = os.getenv('db_password')
dbPort = os.getenv('db_port')
dbHost = os.getenv('db_host')

SQLALCHEMY_DATABASE_URI = 'postgresql://{dbUsername}:{dbPassword}@{dbHost}/{dbName}'

# Application configs
secretKey = os.getenv("secret_key")
debug = os.getenv("environment") == "dev"
applicationRoot = os.getenv("api_application_root", "/api")
host = os.getenv("application_host")
port = int(os.getenv("application_port", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# enable debug mode.
DEBUG = True
