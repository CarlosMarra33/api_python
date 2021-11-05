class Product():
    def __init__(self, name='', img='', description='', price=0, qtd=0, category=''):
        # self.id_product = id_product
        self.name = name
        self.img = img
        self.description = description
        self.price = price
        self.qtd = qtd
        self.category = category

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_img(self):
        return self.img
    def set_img(self, img):
        self.img = img
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_qtd(self):
        return self.qtd
    def set_qtd(self, qtd):
        self.qtd = qtd
    def get_category(self):
        return self.category
    def set_category(self, category):
        self.category = category

    def print(self):
        print("name = ", self.name)
        print("img = ", self.img)
        print("description = ", self.description)
        print("price = ", self.price)
        print("qtd = ", self.qtd)
        print("category = ", self.category)