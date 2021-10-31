class Product():
    def __init__(self, name='', img='', description='', price=0, qtd=0, category=''):
        # self.id_product = id_product
        self._name = name
        self._img = img
        self._description = description
        self._price = price
        self._qtd = qtd
        self._category = category

        def get_name(self):
            return self._name
        def set_name(self, name):
            self._name = name
        def get_img(self):
            return self._img
        def set_img(self, img):
            self._img = img
        def get_description(self):
            return self._description
        def set_description(self, description):
            self.description = description
        def get_price(self):
            return self._price
        def set_price(self, price):
            self._price = price
        def get_qtd(self):
            return self._qtd
        def set_qtd(self, qtd):
            self._qtd = qtd
        def get_category(self):
            return self._category
        def set_category(self, category):
            self._category = category

    def print(self):
        print("name = ", self.name)
        print("img = ", self.img)
        print("description = ", self.description)
        print("price = ", self.price)
        print("qtd = ", self.qtd)
        print("category = ", self.category)