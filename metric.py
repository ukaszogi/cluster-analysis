import distance as dst

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
        self.dist = lambda x, y: dst.distan[func](x, y)
