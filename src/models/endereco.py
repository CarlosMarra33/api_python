class Endereco():
    def __init__(self, street='', number=0, complement=''):
        self.street = street
        self.number = number
        self.complement = complement

        def getstreet(self):
            return self.street
        def setstreet(self, street):
            self.street = street
        def getnumber(self):
            return self.number
        def setnumber(self, number):
            self.number = number
        def getcomplement(self):
            return self.complement
        def setcomplement(self, complement):
            self.complement = complement


    def __str__(self):
        return f'rua = {self.street}, numero = {self.number}, complement = {self.complement}'
