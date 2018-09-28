#Basic functions that are going to be used a lot by other classes and methods

def search_orders(orders,order_id):
    for order in orders:
        if order['order_id'] == order_id:
            return order

#this function takes in a an item_no. and returns both the id and the item(items in the dictionary)
def modify_helper(orders, order_id, status):
    for order in orders:
        if order['order_id'] == order_id:

            order['status'] = status
    return orders