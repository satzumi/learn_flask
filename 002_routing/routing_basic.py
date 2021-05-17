''''
Routing happen in app.url_map which instance of Werkzeug's Map class.
1.By default mapper only allows GET,OPTIONS and HEAD calls on a declared route.
2.Calling valid endpoint with unsupported method with return 404 Method not allowed.
'''


from flask import Flask,jsonify,request

app = Flask(__name__)

# pass methods to support specific methods.
@app.route('/api',methods=['GET','POST','DELETE'])
def my_microservice():
    return jsonify('{hello:world}')

if __name__ == '__main__':
    app.run()