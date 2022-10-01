try:
    from app import app
    import unittest
    import logging
except Exception as e:
    print("Some packages are missing :", e)


class FlaskTest(unittest.TestCase):

    def test_healthcheck(self):
        tester = app.test_client(self)
        response = tester.get("/healthcheck")
        status_code = response.status_code
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()
