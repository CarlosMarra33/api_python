class Endereco():
    def __init__(self, street='', number=0, complement=''):
        self._street = street
        self._number = number
        self._complement = complement

        def get_street(self):
            return self._street
        def set_street(self, street):
            self._street = street
        def get_number(self):
            return self._number
        def set_number(self, number):
            self._number = number
        def get_complement(self):
            return self._complement
        def set_complement(self, complement):
            self._complement = complement


    def __str__(self):
        return f'rua = {self._street}, numero = {self._number}, complement = {self._complement}'
