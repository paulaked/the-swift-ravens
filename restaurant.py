class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []
        self.subtotal = 0
        self.real_total = {}
        self.service_charge = 0.1

    def order(self, item, price, quantity=1):
        add_item = True
        for it in self.bill:
            if it['item'] == item:
                it['price'] += price
                it['quantity'] += quantity
                add_item = False 

        if add_item:   
            self.bill.append({'item': str(item),
            'price': float(price),
            'quantity': quantity})
        print(f'order is {self.bill}')

    def remove(self, item, price, quantity):
        new_price = 0
        for it in self.bill:
            if it['item'] == item:
                old_quant = it['quantity']
                new_quant = old_quant - quantity
                it['quantity'] = new_quant
                old_price = it['price']
                new_price -= old_price - price
                it['price'] = new_price

    def get_subtotal(self):
        for bill in self.bill:
            calculate = bill['price'] * bill['quantity']
            self.subtotal += calculate
            return self.subtotal

            
    def get_total(self, service_charge = 0.1): # needs sorting messed around with it
        self.service_charge = service_charge * self.subtotal
        pound_sign = u'\u00a3'
        self.real_total['Sub Total'] = f'{pound_sign}{self.subtotal:.2f}'
        self.real_total['Service Charge'] = '{}{:.2f}'.format(pound_sign, self.service_charge)
        total = self.service_charge + self.subtotal
        self.real_total['Total'] = f'£{self.subtotal + total}'

        return self.real_total

    def split_bill(self): # not sorted yet actuallygit
        print(self.service_charge, self.subtotal)
        floating = float(self.subtotal)
        total = (floating * self.service_charge) * floating
        print(total)
        divider = total / self.number_of_diners
        return round(self.service_charge)


tab = Table(6)
tab.order('Food1', 20.00, 3)
tab.order('Food2', 10.00, 1)
tab.order('Food3', 3.20, 1)
print(tab.split_bill())
# tab1 = Table('1')
# tab1.order('Food1', 10.00, 3)
# tab1.order('Food2', 20.00, 1)
# tab1.order('Food3', 0.50, 1)
# tab1.order('Food1', 10.00, 3)
# print(tab1.bill)
# # tab1.get_subtotal()
# # print(tab1.get_total())
# # print(tab1.split_bill(4))