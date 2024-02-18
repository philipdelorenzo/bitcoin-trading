import os
import configparser

# Read the config file
BASE = os.path.abspath(os.path.dirname(__file__))
MAIN = os.path.abspath(os.path.join(BASE, ".."))
_config = configparser.ConfigParser()
_config.read(os.path.join(MAIN, 'config.ini'))

api_key = _config["api"]["api_key"]
