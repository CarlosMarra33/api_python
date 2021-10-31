class Product():
    def __init__(self, name, img, description, price, qtd, category):
        # self.id_product = id_product
        self.name = name
        self.img = img
        self.description = description
        self.price = price
        self.qtd = qtd
        self.category = category

    def print(self):
        print("name = ", self.name)
        print("img = ", self.img)
        print("description = ", self.description)
        print("price = ", self.price)
        print("qtd = ", self.qtd)
        print("category = ", self.category)