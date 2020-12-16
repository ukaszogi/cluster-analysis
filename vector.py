class vector:
    def __init__(self, cords):
        self.__dim = len(cords)
        self.__cords = cords
    
    def __str__(self):
        w = "("
        for i in range(self.__dim-1):
            w += str(self.__cords[i]) + ", "
        w += str(self.__cords[self.__dim-1]) + ")"
        return w
    
    def __abs__(self):
        x = 0
        for i in range(self.__dim):
            x += self.__cords[i]**2
        return x**(1/2)
    
    def __add__(self, u):
        return vector(list(map(lambda a, b: a + b, self.__cords, u.__cords)))
    
    def __iadd__(self, u):
        for i in range(self.__dim):
            self.__cords[i] += u.__cords[i]
    
    def __mul__(self, k):
        return vector(list(map(lambda x: k*x, self.__cords)))
    

v = vector([3,4])
u = vector([4,3])
print(v)
print(abs(v))
print(u + v)
print(v*5)
print(5*v)