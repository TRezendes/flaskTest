from flask import Flask, render_template, url_for, redirect, session
from rikeripsum.rikeripsum import generate_paragraph as RikerIpsum
from flask_wtf.csrf import CSRFProtect
import json

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, subdomain_matching=True)

    uwllpt17800_config_path = 'C:\\Users\\trezendes\\projects\\flaskTest\\config.json'
    titan_config_path = '~/Projects/flaskTest/config.json'

    with open(
        uwllpt17800_config_path
        #titan_config_path
    ) as config_file:
        config = json.load(config_file)

    app.config['SECRET_KEY'] = config.get('SECRET_KEY')
    app.config['SERVER_NAME'] = config.get('SERVER_NAME')

    csrf.init_app(app)
    csrf.app = app

    with app.app_context():
        # Register blueprints
        from .luciano import luciano as luciano
        app.register_blueprint(luciano, url_prefix='/luciano')

    # Add RikerIpsum template global
    @app.template_global('RikerIpsum')
    def riker_ipsum(sentences):
        return RikerIpsum(sentences)
    
    """ luciano
    Content in this section is for StackOverflow question https://stackoverflow.com/questions/77358658/python-flask-is-it-possible-to-get-string-from-a-function-in-views-py-to-a-td
    (Blueprint 'luciano')

    See below for a link to my answer
    """


    # @app.context_processor
    # def exampleProcessor():
    #     def exampleFunction(itemID):
    #         return 'test correct' + str(itemID)
    #     return dict(exampleFunction=exampleFunction)

    @app.template_global('exampleFunction')     # Although there are several ways to accomplish the task that the OP was asking about,
    def exampleFunction(itemID):                # my answer used flask.Flask.template_global
        return 'test correct' + str(itemID)     # See the answer at https://stackoverflow.com/a/77361830/16832874

    """ luciano
    """

    return app
