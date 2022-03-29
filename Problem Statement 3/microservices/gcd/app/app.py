from flask import Flask
from flask_restful import Resource, Api
import socket

app = Flask(__name__)
api = Api(app)

def get_gcd(a, b):
    # Everything divides 0
    if (b == 0):
         return a
    return get_gcd(b, a%b)
    
class GCD(Resource):
    def get(self, number_1, number_2):
        return get_gcd(number_1, number_2)

api.add_resource(GCD, '/<int:number_1>/<int:number_2>')

if __name__ == '__main__':
    app.run(debug=True,port=5055,host="0.0.0.0")