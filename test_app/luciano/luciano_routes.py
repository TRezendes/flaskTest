from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for
from . import luciano
from .abc import foo


cart = {
    "item1": {
        "name": "Thingamabob",
        "id": 1
        },
    "item2": {
        "name": "Whatchamacallit",
        "id": 2
        },
    "item3": {
        "name": "foo",
        "id": 3
        },
    "item4": {
        "name": "bar",
        "id": 4
        }
    }


""" luciano
The function definitions below expand on the original answer to Luciano's question by showing how to pass functions to individual templates.
See ../__init__.py for the link to the question and answer.
"""


def bar(input):
    stringBAR = f"The input to the bar function was: {input}"
    return stringBAR

@luciano.route('/home')
def home():
    return render_template(
        '/luciano/home.jhtml',
        cart=cart,
        foo=foo,
        bar=bar
        )

@luciano.route('item-detail/<itemID>')
def item_detail(itemID):
    return render_template(
        '/luciano/<itemID>.jhtml',
        cart=cart
    )




