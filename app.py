from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class func(Resource):
    def post(self):
        try:
            return {'StatusCode':'200', 'Message': 'OK'}


        except Exception as e:
            return {'error': str(e)}

api.add_resource(func, '/func')

@app.route('/')
def home(name=None):
   return render_template('form.html')
   
if __name__ == '__main__':
   app.run()