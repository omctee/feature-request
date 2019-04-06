import re
import unittest
from requester import create_app, db
from requester.models import User, Client, Request
from populate import populate_db

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        populate_db()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        print('Status code -- ' + response.status_code)
        self.assertEqual(response.status_code, 200)

"""
	//TODO: add more test
"""