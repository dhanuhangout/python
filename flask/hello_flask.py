'''Hello world flask.'''
from flask import Flask
from flask import jsonify
from flask import request

FLASK_APP = Flask(__name__)


QUARKS = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]

@FLASK_APP.route('/', methods=['GET'])
def hello_world():
    '''Hello workld function.'''
    return jsonify({'message' : 'Hello, World!'})

@FLASK_APP.route('/quarks', methods=['GET'])
def return_all():
    '''return_all.'''
    return jsonify({'quarks' : QUARKS})

@FLASK_APP.route('/quarks/<string:name>', methods=['GET'])
def return_one(name):
    '''return_one.'''
    the_one = QUARKS[0]
    for i, qua in enumerate(QUARKS):
        if qua['name'] == name:
            the_one = QUARKS[i]
    return jsonify({'quarks' : the_one})

@FLASK_APP.route('/quarks', methods=['POST'])
def add_one():
    '''add_one.'''
    new_quark = request.get_json()
    QUARKS.append(new_quark)
    return jsonify({'quarks' : QUARKS})

@FLASK_APP.route('/quarks/<string:name>', methods=['PUT'])
def edit_one(name):
    '''edit_one.'''
    new_quark = request.get_json()
    for i, qua in enumerate(QUARKS):
        if qua['name'] == name:
            QUARKS[i] = new_quark
    #pylint: disable=unused-variable
    quas = request.get_json()
    #pylint: enable=unused-variable
    return jsonify({'quarks' : QUARKS})

@FLASK_APP.route('/quarks/<string:name>', methods=['DELETE'])
def delete_one(name):
    '''delete_one.'''
    for i, qua in enumerate(QUARKS):
        if qua['name'] == name:
            del QUARKS[i]
    return jsonify({'quarks' : QUARKS})

if __name__ == "__main__":
    FLASK_APP.run(debug=True)
