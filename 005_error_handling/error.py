from flask import Flask,jsonify


app = Flask(__name__)

@app.errorhandler(500)
def err_handler(error):
    return jsonify({'Error':str(error)},500)

@app.route('/api')
def my_microservice():
    raise TypeError('some exception')

if __name__  == '__main__':
    app.run()