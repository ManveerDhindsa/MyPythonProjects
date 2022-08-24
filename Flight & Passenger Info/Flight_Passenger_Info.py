class Flight:
    def __init__(self, origin, destination, nop=100):
        self.origin = origin
        self.destination = destination
        self.nop = nop    
    
    def __str__(self):
        return f'This flight has {self.nop} passengers and is going from {self.origin} to {self.destination}'
    
    def plane(Self):
        return 'This is AirCanada'
    
    @property
    def origin(self):
        return self._origin
    
    @origin.setter
    def origin(self, origin):
        if origin not in ['Tor', 'LA']:
            raise ValueError('Not a valid origin')
        self._origin = origin
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, destination):
        if destination not in ['Van', 'Mtl']:
            raise ValueError('Not a valid destination')
        self._destination = destination    
    
    
class Passenger(Flight):
    
    airplane = 'AirCanada'
    
    def __init__(self, name, age, origin, destination):
        super().__init__(origin, destination)
        self.name = name
        self.age = age
    
    def person(self):
        return f'{self.name} is {self.age} years old and is landing in {self.destination}'
    
    @classmethod
    def flying(cls, name):
        return f'{name} likes flying on {cls.airplane}'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name not in ['Tom', 'John', 'Bob']:
            raise ValueError('Not a valid name')
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

def main():    
    name = input('Name: ')
    age = input('Age: ')
    origin = input('Origin: ')
    destination = input('Destination: ')
    
    info1 = Flight(origin, destination)
    print(info1)

    info2 = Passenger(name, age, origin, destination)
    print(info2.person())
    print(info2.flying(name))    

if __name__ == '__main__':
    main()
    
