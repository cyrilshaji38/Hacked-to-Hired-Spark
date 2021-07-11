from SparkApp import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly.
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly.
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'SIGN IN', response.data)

    # Ensure that the register page loads correctly.
    def test_register_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/register')
        self.assertIn(b'SIGN UP', response.data)

    # Ensure username has more than one character.
    def test_correct_username(self):
        tester = app.test_client()
        response = tester.post(
            '/register',
            data=dict(username="a"),
            follow_redirects=True
        )
        self.assertIn(b'Username must contain between 2 to 30 characters!', response.data)

    # Ensure email is valid.
    def test_correct_email(self):
        tester = app.test_client()
        response = tester.post(
            '/register',
            data=dict(email="cyril"),
            follow_redirects=True
        )
        self.assertIn(b'Not a valid email address!', response.data)

    # Ensure mobile number is of 10 digits.
    def test_correct_mobile(self):
        tester = app.test_client()
        response = tester.post(
            '/register',
            data=dict(mobile="1"),
            follow_redirects=True
        )
        self.assertIn(b'Mobile No. must be 10 digits', response.data)

    # Ensure password is atleast 6 characters.
    def test_correct_password(self):
        tester = app.test_client()
        response = tester.post(
            '/register',
            data=dict(password="123"),
            follow_redirects=True
        )
        self.assertIn(b'Password must have atleast 6 characters!', response.data)

    # # Ensure that the teacher dashboard page loads correctly
    # def test_teacher_page_loads(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/teacher')
    #     self.assert(b'Welcome Teacher!', response.data)

    # # Ensure that the student dashboard page loads correctly
    # def test_student_page_loads(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/student')
    #     self.assertIn(b'Welcome Student!', response.data)

    # # Ensure that the assesment page loads correctly
    # def test_assesment_page_loads(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/assesment')
    #     self.assertIn(b'Answer the following questions with a value ranging from 1 to 10', response.data)

    # # Ensure that the critical thinking game page loads correctly
    # def test_critical_thinking_game_page_loads(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/critical_thinking')
    #     self.assertIn(b'Game to improve critical thinking skills', response.data)

    # # Ensure that the communication game page loads correctly
    # def test_communication_game_page_loads(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/communication')
    #     self.assertIn(b'Game to improve communication skills', response.data)


if __name__ == '__main__':
    unittest.main()