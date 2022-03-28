from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
class Modulus(Resource):
    def get(self, number_1, number_2):
        return number_1%number_2

api.add_resource(Modulus, '/<int:number_1>/<int:number_2>')

if __name__ == '__main__':
    app.run(debug=True,port=5057,host="0.0.0.0")