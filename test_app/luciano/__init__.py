# This blueprint for testing to answer the StackOverflow quetion posed by user  luciano-oliveira at https://stackoverflow.com/questions/77358658/python-flask-is-it-possible-to-get-string-from-a-function-in-views-py-to-a-td


from flask import Blueprint


luciano = Blueprint('luciano', __name__, template_folder='templates', static_folder='static')

from . import luciano_routes
