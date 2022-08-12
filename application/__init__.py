from flask import Flask
import os.path


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.isfile(os.path.join(BASE_DIR, 'config_prod.py')):
    app.config.from_object('config_prod')
else:
    app.config.from_object('config')

handler = app.config['LOGGING_HANDLER']
handler.setFormatter(app.config['LOGGING_FORMATTER'])
if len(app.logger.handlers) > 0:
    app.logger.handlers[0] = handler
else:
    app.logger.addHandler(handler)

app.logger.setLevel(app.config['LOGGING_LEVEL'])


from application import views, models