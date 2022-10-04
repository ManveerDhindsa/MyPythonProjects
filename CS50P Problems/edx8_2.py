class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity must be greater than zero")
        self._capacity = capacity
        self._size = 0
        
        
    def __str__(self):
        return self._size*'🍪'
    
    
    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("over capacity")        

        if self._size + n> self._capacity:
            raise ValueError("over capacity")  
        self._size = self._size + n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies in jar")
        self._size = self._size - n
        

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size
        

# jar = Jar()
# jar.deposit(3)
# print(jar)

# def main():
#     jar = get_jar()
#     print(jar)
    
# def get_jar():
#     n = input("how many cookies to add to jar: ")
#     jar1 = Jar()
#     return jar1.deposit(n)


# if __name__ == "__main__":
#     main()