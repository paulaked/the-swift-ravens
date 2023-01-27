class Table:
    def __init__(self, table_num):
        self.bill = []
        self.subtotal= 0
        self.table_num = table_num
        

    def order(self, item, price, quantity = 1):
        order_list = {"item": item, "price": price, "quantity": quantity}
        self.item = item
        self.bill.append (order_list)
        return self.bill


    def remove(self, item, price, quantity):
        old_quantity = self.bill[0]['quantity']
        new_quantity = old_quantity - quantity
        self.bill[0]['quantity'] = new_quantity

    def get_subtotal(self):
        for num in self.bill:
            self.subtotal += num['price'] * num['quantity']
        print(self.subtotal)
        return self.subtotal
        

    def get_total(self, discount):
        discount_price = self.subtotal * discount
        total_price = self.subtotal + discount_price
        print ({'Sub Total': self.subtotal, 'Service Charge': discount_price, 'Total': total_price})
        return {'Sub Total': self.subtotal, 'Service Charge': discount_price, 'Total': total_price}


    def split_bill(self):
        bill_split = self.total_price / self.guests_per_table
        print(bill_split)


tab = Table(2)
tab.order('egg', 10.00, 3)
tab.order('Food', 10.00, 5)
tab.order('Food', 5, 1)
print(tab.get_subtotal())
print(tab.get_total(0.15))
print(tab.split_bill)()