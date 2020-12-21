import distance as dst

distan = {
    "Euklidean": lambda x, y: dst.Minkowski(x, y, 2),
    "Minkowski": lambda x, y, p: dst.Minkowski(x, y, p),
    "Manhattan": lambda x, y: dst.Minkowski(x, y, 1),
    "Maximum": lambda x, y: dst.Maximum(x, y)
}

class metric:
    def setPoints(self, points):
        self.__points = points
    def __str__(self):
        for i in self.__points:
            print(i)

class clusters:
    def fit(self, data):
        pass
    
    def metric(self, func):
        self.dist = lambda x, y: distan[func](x, y)
