import unittest
import index
import json
from mongoengine import connect


class TestUserSignOut(unittest.TestCase):

    def setUp(self):
        connect('test_ser517', host='mongodb://localhost/test_ser517')
        index.app.config['TESTING'] = True
        index.app.config["MONGODB_DB"] = 'test_ser517'
        self.app = index.app.test_client()

# Test sign out for admin who is not currently logged in
    def test_admin_signout_not_logged(self):

        res = self.app.post('/admin/signoutaccess', data=json.dumps({
                                                    "email": "zux@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Test sign out for admin who is logged in
    def test_admin_signout(self):

        res = self.app.post('/admin/signoutaccess', data=json.dumps({
                                                    "email": "zux@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

# Test sign out for admin with incorrect email
    def test_incorrect_admin_signout(self):

        res = self.app.post('/admin/signoutaccess', data=json.dumps({
                                                    "email": "zux@mail.com"}),
                            content_type='application/json')
        self.assertEqual(res.status_code, 401)


if __name__ == "__main__":
    unittest.main()
