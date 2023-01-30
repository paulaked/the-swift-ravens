import math
class Table:
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        self.bill = []
        self.abs_total = 0
    def order(self, item, price, quantity=1):
        add_item = True
        for it in self.bill:
            if it['item'] == item:
                it['price'] += price
                it['quantity'] += float(quantity)
                add_item = False 

        if add_item:   
            self.bill.append({'item': str(item),
            'price': float(price),
            'quantity': quantity})
        print(f'order is {self.bill}')

    def remove(self, item, price, quantity):
        new_price = 0
        for it in self.bill:
            if it['item'] == item and it['price'] == price:
                if it['quantity'] < quantity:
                    return False
                elif it['quantity'] == quantity:
                    del it
                    return True
                else:                    
                    it['quantity'] -= float(quantity)
                    return True
        return False 

        

    def get_subtotal(self):
        subtote = 0
        for num in range(len(self.bill)):
            calculate = self.bill[num]['price'] * self.bill[num]['quantity']
            subtote += calculate/100*100    
        return float('{0:.2f}'.format(subtote))

            
    def get_total(self, service_charge = 0.1):
        pound_sign = u'\u00a3'
        subtote = self.get_subtotal()
        service_charge = service_charge * subtote
        self.abs_total = round(service_charge + subtote, 2)
        return {    
            "Sub Total": f"{pound_sign}{subtote:.2f}",
            "Service Charge": f"{pound_sign}{service_charge:.2f}",
            "Total": f"{pound_sign}{self.abs_total:.2f}"
        }

    def split_bill(self):
        divider = self.abs_total / self.number_of_diners
        print(self.number_of_diners)
        print(float(self.abs_total))
        # return float(f'{divider:.2f}')
        return float(f'{self.abs_total / self.number_of_diners:.2f}')

# tab3 = Table(3)
# tab3.order('Food', 10.00, 5)
# tab3.remove('Food', 10.00, 3)
# print(tab3.get_subtotal())
# tab3.get_total()
# print(tab3.bill)
# tab = Table(6)
# tab.order('Food1', 20.00, 3)
# tab.order('Food2', 10.00, 1)
# tab.order('Food3', 3.20, 1)
# tab.get_subtotal()
# print(tab.get_total())
# print(tab.bill)
# print(tab.split_bill())

# tab1 = Table('1')
# tab1.order('Food1', 10.00, 3)
# tab1.order('Food2', 20.00, 1)
# tab1.order('Food3', 0.50, 1)
# tab1.order('Food1', 10.00, 3)
# print(tab1.bill)
# # tab1.get_subtotal()
# # print(tab1.get_total())
# # print(tab1.split_bill(4))