try:
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    import logging
    from dotenv import load_dotenv
    from models.customer import db, Customer
    import warnings
    import os
    from functools import wraps
except Exception as e:
    print("Some packages are missing :", e)

# Ignore all warnings
warnings.filterwarnings("ignore")

# Load varibles from environment file
load_dotenv()
logging_filepath = str(os.getenv('APP_LOG_FILEPATH'))
database_uri = str(os.getenv('SQLALCHEMY_DATABASE_URI'))
app_port = int(os.getenv('PORT'))

# Logger Configuration
logging.basicConfig(filename=logging_filepath, format='%(asctime)s - %('
                                                      'levelname)s - %(message)s',
                    datefmt='%m-%d-%Y '
                            '%I:%M:%S %p %Z',
                    level=logging.INFO)

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/postgres'
db.init_app(app)


@app.route('/healthcheck', methods=['GET'])
def health_check():
    return "Up and running!"


def check_auth(username, password):
    load_dotenv()
    try:
        api_user = str(os.getenv('BASIC_AUTH_USERNAME'))
        api_password = str(os.getenv('BASIC_AUTH_PASSWORD'))
    except Exception as ex:
        print(ex)
    return username == api_user and password == api_password


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            message = {"status": 401, "error": "Basic Auth Required.", "data": {}}
            resp = jsonify(message)
            resp.status_code = 401
            return resp

        return f(*args, **kwargs)

    return decorated


@app.route('/customer', methods=['POST'])
@requires_auth
def create_customer():
    body = request.get_json()
    db.session.add(Customer(body['first_name'], body['last_name'], body['phone_number'], body['email']))
    db.session.commit()
    return "customer created"


@app.route('/customers/<customer_id>', methods=['GET'])
@requires_auth
def get_customer(customer_id):
    result = db.session.query(Customer).filter_by(customer_id=customer_id).all()
    for row in result:
        final_json = {"customer_id": row.customer_id, "first_name": row.first_name, "last_name": row.last_name,
                      "email": row.email}
    return jsonify(final_json)


@app.route('/customers', methods=['GET'])
@requires_auth
def get_customers():
    customers = []
    for customer in db.session.query(Customer).all():
        del customer.__dict__['_sa_instance_state']
        customers.append(customer.__dict__)
    return jsonify(customers)


@app.route('/customers/<customer_id>', methods=['POST'])
@requires_auth
def update_customer(customer_id):
    body = request.get_json()
    db.session.query(Customer).filter_by(customer_id=customer_id).update(
        dict(first_name=body['first_name'], last_name=body['last_name'], phone_number=body['phone_number'],
             email=body['email']))
    db.session.commit()
    return "customer updated"


@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer_by_id(customer_id):
    db.session.query(Customer).filter_by(customer_id=customer_id).delete()
    db.session.commit()
    return "customer deleted"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=82)
