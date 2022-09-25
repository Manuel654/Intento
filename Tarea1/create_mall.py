class Create_mall:
    def __init__(self):
        self.shop_quantity = int(input('Shop quantity: '))
        self.mall={}
    def shop_type(self):
        for i in range(self.shop_quantity):
            self.mall[i]=input('shop category: ')
        return self.mall
        
