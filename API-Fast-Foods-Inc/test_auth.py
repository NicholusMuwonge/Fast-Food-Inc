import unittest, json
from application import app 
from application import Blueprint 
from application.users.routes import db
import flask

class Test_auth(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('SetUp')
        self.client = app.test_client()
        app.testing = True
        test = flask.Blueprint('application.users.routes.db',__name__) 
        
    @classmethod
    def tearDownClass(self):
        print('TearDown')
     
    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # user registration
            resp_register = self.client.post(
                '/auth/signup',
                data=json.dumps(dict(
                    username="nicholus",
                    email='nicholusmuwonge@gmail.com',
                    password='123456'
                )),
                content_type='application/json',
            )
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.'
            )
            self.assertTrue(data_register['auth_token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = self.client.post(
                '/auth/login',
                data=json.dumps(dict(
                    username = "nicholus",
                    password='123456'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_place_an_order(self):

        """ Test for placing an order"""
        with self.client:
            resp = self.client.post(
                    '/users/orders',
                    data=json.dumps({'user_id':1,'order_id':'1','item_id':'1','item_name':'chips','item_quantity':'2kgs','price':'2000'} ),
                    content_type='application/json'
                )
            rdata = json.loads(resp.data.decode())
            self.assertTrue(
                    rdata['message'] == 'order placed'
                )
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 201)

    def test_get_all_orders(self):
        """ Test for getting all orders"""
        with self.client:
            resp = self.client.get('/orders/')
            rdata = json.loads(resp.data.decode())
            self.assertTrue(rdata['status'] == 'success')
            self.assertTrue(
            rdata['message'] == 'all orders retrieved')               
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 200)

    def test_get_specifc_order(self):
        """ Test for getting specific order"""
        with self.client:
            resp = self.client.get('/orders/1')   
            rdata = json.loads(resp.data.decode())
            self.assertTrue(rdata['status'] == 'success')
            self.assertTrue(rdata['message'] == 'order retrieved')
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 200)    

    def test_update_order(self):
        """ Test for order update"""
        with self.client:
            resp = self.client.put('/orders/1',  data=json.dumps({"status":"processing"}),
                    content_type='application/json' )   
            rdata = json.loads(resp.data.decode())
            self.assertTrue(rdata['status'] == 'processing')
            self.assertTrue(
                    rdata['message'] == 'updated successfully'
                )
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 201)  

    def test_get_menu(self):
        pass
        """ Test for get menu"""
        with self.client:
            resp = self.client.get('/menu')   
            rdata = json.loads(resp.data.decode())
            self.assertTrue(
                    rdata['message'] == 'menu retrieved'
                )
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 200)  

    def test_add_food_item_to_menu(self):
        """ Test for adding food item"""
        with self.client:
            resp = self.client.post('/menu',data=json.dumps(
                       { "item_name":"hamburger", "item_price":200 } ),content_type='application/json')   
            rdata = json.loads(resp.data.decode())
            self.assertTrue(rdata['message'] == 'food item added' )
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 201)  

    def test_get_order_history(self):
        pass
        """ Test for get menu"""
        with self.client:
            resp = self.client.get('/users/orders')   
            rdata = json.loads(resp.data.decode())
            self.assertTrue(
                    rdata['message'] == 'order history retrieved successfully'
                )
            self.assertTrue(rdata['auth_token'])
            self.assertTrue(resp.content_type == 'application/json')
            self.assertEqual(resp.status_code, 200)  

if __name__ == '__main__':
    unittest.main()
