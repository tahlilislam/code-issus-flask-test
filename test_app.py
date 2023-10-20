"""Sample test suite for testing demo."""

from unittest import TestCase
from app import app
from flask import session

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ColorViewsTestCase(TestCase):
    """Examples of integration tests: testing Flask app."""

    def test_color_form(self):
        with app.test_client() as client:
            # can now make requests to flask via `client`
            # client represents the server/app
            # can import pdb pdb.set_trace() debugger to see what we have access to 
            # import pdb
            # pdb.set_trace()

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)
            #checking if string is in html

    def test_color_submit(self):
        with app.test_client() as client:
            resp = client.post('/fav-color',
                               data={'color': 'blue'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Woah! I like blue, too', html)

    def test_redirection(self):
        with app.test_client() as client:
            resp = client.get("/redirect-me")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")
            # self.assertEqual(resp.location, "http://http://127.0.0.1/")

    # would also want to test if we r redirected to "/", 
    # we are getting a 200 status code if redirection is followed thru
    def test_redirection_followed(self):
        with app.test_client() as client:
            resp = client.get("/redirect-me", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)

    # def test_session_info(self):
    #     with app.test_client() as client:
    #         resp = client.get("/")

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(session['count'], 1)

    # def test_session_info_set(self):
    #     with app.test_client() as client:
    #         # Any changes to session should go in here:
    #         with client.session_transaction() as change_session:
    #             change_session['count'] = 999

    #         # Now those changes will be in Flask's `session`
    #         resp = client.get("/")

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertEqual(session['count'], 1000)
