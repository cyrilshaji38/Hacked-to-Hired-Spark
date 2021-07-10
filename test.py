from SparkApp import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'SIGN IN', response.data)

    # Ensure that the register page loads correctly
    def test_register_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/register')
        self.assertIn(b'SIGN UP', response.data)


if __name__ == '__main__':
    unittest.main()