from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Logger Configuration
logging.basicConfig(filename='C:/Users/Lakshay/Desktop/CRUD-Customer/logs/app.log', format='%(asctime)s - %('
                                                                                           'levelname)s - %(message)s',
                    datefmt='%m-%d-%Y '
                            '%I:%M:%S %p %Z',
                    level=logging.INFO)


app = Flask(__name__)
CORS(app)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return "Up and running!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=82)
