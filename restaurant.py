class Table:
    def __init__(self, table):
        self.table = 0
        self.bill = []
        self.total = []

    def order(self, item, price, quantity=1):
        self.bill.append({'item': item,
            'price': price,
            'quantity': quantity})
        # print(f'order is {self.bill}')

    def remove(self, item, price, quantity):
        print('remove is now operating')
        old_quant = self.bill[0]['quantity']
        new_quant = old_quant - quantity
        del self.bill[0]['quantity']
        self.bill.append({'quantity': new_quant})

        if item not in self.bill[0]['item'] and price not in self.bill[0]['price']:
            return False
        else:
            return True


    def get_subtotal(self):
        for a in range(len(self.bill[0])):
            calculate = self.bill[a]['price'] * self.bill[a]['quantity']
            self.total.append(float(calculate))
            
    def get_total(self):
        print(self.totals)
        return round(sum(self.total),2)

    def split_bill(self, number_of_splits):
        pass

tab1 = Table('1')
tab1.order('Food1', 10.00, 3)
tab1.order('Food2', 20.00, 1)
tab1.order('Food3', 0.50, 1)
tab1.get_subtotal()
print(tab1.get_total())