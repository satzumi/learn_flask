
from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter,ValidationError

_USERS = {'1':'Satindar','2':'Mac'}
_IDS = {val:id for id, val in _USERS.items()}


#should be inherited form BaseConverter
class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            name = _USERS[value]
            return name
        
        raise ValidationError()

    def to_url(self, value):
        return _IDS[value]


app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/person/<registered:name>')
def  person(name):
    response = jsonify({'hello':name})
    return response

if __name__ == '__main__':
    app.run()
