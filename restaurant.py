class Table:
    def __init__(self, table_no):
        self.bill = []     #created a bill in a list
        self.subtotal = 0  # setting the subtotal to float
        self.table_no = table_no
    

    def order(self, item, price, quantity =1): # quantity default to 1
        menu_order = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(menu_order)   #stored in the order 
        return self.bill

    
    def remove(self, item, price, quantity):
        old_quantity = self.bill[0]['quantity']
        new_quantity = old_quantity - quantity
        self.bill[0]['quantity'] = new_quantity  #key to get that value
        print(old_quantity)

    def get_subtotal(self):
        subtotal = 0          # setting the subtotal to float
        for item in self.bill:
            subtotal += item['price'] * item['quantity']
        return subtotal


   
    def get_total(self, discount):
        discount_price = self.subtotal * discount
        total_price = self.subtotal + discount_price
        print ({'Sub Total': self.subtotal, 'Service Charge': discount_price, 'Total': total_price})
        return {'Sub Total': self.subtotal, 'Service Charge': discount_price, 'Total': total_price}



    def split_bill(self):
        def split_bill(self):
        bill_split = self.total_price / self.guests_per_table
        print(bill_split)
        




# tab = Table(2)
# tab.order('Food', 10.00, 5)
# tab.remove('Food', 10.00, 3)
# print(tab.bill)