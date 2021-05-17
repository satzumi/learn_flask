from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/person/<person_id>')
def person(person_id):
    response = jsonify({'hello':person_id})
    return response

if __name__ == '__main__':
    app.run()

