class Table:
    def __init__(self, table):
        self.table = 0
        self.bill = []
        self.subtotal = []
        self.real_total = {}
        self.service_charge = 0.1

    def order(self, item, price, quantity=1):
        for a in range(len(self.bill)):
            if item[a] == item:
                self.bill[a]['price'] += price
                self.bill[a]['quantity'] += quantity   
        print(self.bill[0].keys())
        # if item not in self.bill[0].keys():
        #     self.bill.append({'item': str(item),
        #     'price': float(price),
        #     'quantity': quantity})
        
        # print(f'order is {self.bill}')

    def remove(self, item, price, quantity):
        old_quant = self.bill[0]['quantity']
        new_quant = old_quant - quantity
        self.bill[0]['quantity'] = new_quant

        old_price = self.bill[0]['price']
        new_price = float(old_price - price)
        self.bill[0]['price'] = new_price
        # if item not in self.bill[0]['item'] and price not in self.bill[0]['price']:
        #     return False
        # else:
        #     return True


    def get_subtotal(self):
        for a in range(len(self.bill[0])):
            calculate = self.bill[a]['price'] * self.bill[a]['quantity']
            self.subtotal.append((calculate))

            
    def get_total(self, service_charge = 0.1):
        self.service_charge = service_charge
        pound_sign = u'\u00a3'
        self.real_total['Sub Total'] = f'{pound_sign}{sum(self.subtotal):.2f}'
        self.real_total['Service Charge'] = '{}{:.2f}'.format(pound_sign, sum(self.subtotal) * service_charge)
        total_service = sum(self.subtotal) * service_charge
        total = total_service + sum(self.subtotal)
        self.real_total['Total'] = f'£{sum(self.subtotal) + total}'

        return self.real_total

    def split_bill(self, number_of_diners):
        total = (sum(self.subtotal) * self.service_charge) * sum(self.subtotal)
        divider = total / number_of_diners
        return round(divider, 2)

tab1 = Table('1')
tab1.order('Food1', 10.00, 3)
tab1.order('Food2', 20.00, 1)
tab1.order('Food3', 0.50, 1)
print(tab1.bill)
# tab1.get_subtotal()
# print(tab1.get_total())
# print(tab1.split_bill(4))