import unittest, json
from application import app 
from application import Blueprint 
from application.api.routes import mod
import flask

class test_api(unittest.TestCase):#defn of your own tests

    @classmethod
    def setUpClass(self):  
        print('SetUp')
        app.testing = True
        test = flask.Blueprint('application.api.routes.mod',__name__) 
          
        self.orders = {"user_id": "U1", "item_ordered": "chicken and beef","item_quantity":"2kg"}      
        self.client = app.test_client()  
	    

    @classmethod
    def tearDownClass(self):
        print('TearDown')

    #the setUpClass and tearDownClass only run once since they are class methods                    

    def test_init_page(self):
        rv = self.client.get('/api/v1/')
        self.assertEqual(rv.status_code, 200)


    def test_get_orders(self):
        rv = self.client.get('/api/v1/orders')
        self.assertEqual(rv.status_code, 200)
       
    def test_place_order(self):
        rv = self.client.post('/api/v1/orders', data=json.dumps(self.orders), content_type="application/json")
        self.assertEqual(rv.status_code, 201)


    def test_get_an_order(self):
        
        rv = self.client.post('/api/v1/orders', data=json.dumps(self.orders), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        rv2 = self.client.get('/api/v1/orders/1')
        self.assertEqual(rv2.status_code, 200)
         

    
    def test_modify_order(self):
        rv = self.client.post('/api/v1/orders', data=json.dumps(self.orders), content_type="application/json")
        self.assertEqual(rv.status_code, 201)
        rv2 = self.client.put('/api/v1/orders/1', data= json.dumps({'status':'completed'}), content_type="application/json")
        self.assertEqual(rv2.status_code, 201)
         

if __name__ == "__main__":
    unittest.main()

# python -m unittest tests/test_api.py