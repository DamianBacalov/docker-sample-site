from flask import render_template
from application import app
import random


@app.route("/", methods=['GET'])
def home():
    app.logger.info('Function: home()')
    app.logger.info('Obteniendo datos desde Postgres')
    return render_template('home.html')


@app.route("/about", methods=['GET'])
def about():
    app.logger.info('Function: about()')
    return render_template('about.html')


@app.route("/contact", methods=['GET'])
def contact():
    app.logger.info('Function: contact()')
    if app.config["RANDOM_ERRORS"]:
        if random.randint(1, 4) == 1:
            app.logger.error('Error accediendo a la base de datos')
            raise "Error interno"
    return render_template('contact.html')


@app.route("/services", methods=['GET'])
def services():
    app.logger.info('Function: services()')
    app.logger.warn('Los servicios deben ser actualizados')
    return render_template('services.html')

