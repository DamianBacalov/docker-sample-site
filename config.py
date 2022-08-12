from flask import request
import logging
import os


LOGGING_LEVEL = logging.DEBUG
LOGGING_HANDLER = logging.StreamHandler()
LOGGING_FORMATTER = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

RANDOM_ERRORS = os.environ.get("RANDOM_ERRORS", "False") == "True"
