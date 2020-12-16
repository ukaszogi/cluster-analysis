class metric:
    def setPoints(self, points):
        self.__points = points
    def __str__(self):
        for i in self.__points:
            print(i)