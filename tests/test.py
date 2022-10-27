try:
    from app import app
    import unittest
    import logging
    import warnings
    from base64 import b64encode
    from dotenv import load_dotenv
    import os
    import json
except Exception as e:
    print("Some packages are missing :", e)


class FlaskTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FlaskTest, self).__init__(*args, **kwargs)
        load_dotenv()
        try:
            api_user = str(os.getenv('BASIC_AUTH_USERNAME'))
            api_password = str(os.getenv('BASIC_AUTH_PASSWORD'))
        except Exception as ex:
            print(ex)
        self.api_user = api_user
        self.api_password = api_password

    def test_healthcheck(self):
        tester = app.test_client(self)
        response = tester.get("/healthcheck", auth=(self.api_user, self.api_password))
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_customers(self):
        tester = app.test_client(self)
        response = tester.get("/customers", auth=(self.api_user, self.api_password))
        status_code = response.status_code
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    # Ignore all warnings
    warnings.filterwarnings("ignore")
    unittest.main()
