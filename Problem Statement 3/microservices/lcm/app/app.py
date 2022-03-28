from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

# Number1 * Number2 = LCM * GCD
# You can get GCD value either from the gcd-service or build your own function here, both are accepted
# This implementation calls the gcd-service
# IF this is used by the students they need to add 'requests' to the requirements.txt file
# BONUS marks for students who implement using this technique
def get_lcm(a, b):
    gcd = int(requests.get(url = f'http://gcd-service:5055/{a}/{b}').text)
    return (a*b)//gcd

    
class LCM(Resource):
    def get(self, number_1, number_2):
        return get_lcm(number_1, number_2)

api.add_resource(LCM, '/<int:number_1>/<int:number_2>')

if __name__ == '__main__':
    app.run(debug=True,port=5056,host="0.0.0.0")