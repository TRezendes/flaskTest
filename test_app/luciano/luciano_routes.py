from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for
from . import luciano


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


# def exampleFunction(itemID):
#     return 'test correct' + str(itemID)


@luciano.route('/home')
def home():
    return render_template(
        '/luciano/home.jhtml',
        cart=cart#,
        #exampleFunction=exampleFunction
        )

@luciano.route('item-detail/<itemID>')
def item_detail(itemID):
    return render_template(
        '/luciano/<itemID>.jhtml',
        cart=cart
    )




