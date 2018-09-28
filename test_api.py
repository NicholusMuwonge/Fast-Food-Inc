import unittest,json   
from flask import request, jsonify
from run import app

class test_api(unittest.TestCase):

    @classmethod
    def setUpClass(self):  
        print('SetUp')
        self.orders = {"user_id": "U1", "item_ordered": "chicken and beef","item_quantity":"2kg"}      
        self.client = app.test_client()
	    
    @classmethod
    def tearDownClass(self):
        print('TearDown')
                

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
        rv2 = self.client.put('/api/v1/orders/1', json={'status':'completed'}, content_type="application/json")
        self.assertEqual(rv2.status_code, 200)
         

if __name__ == "__main__":
    unittest.main()