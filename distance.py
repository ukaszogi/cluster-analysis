def Minkowski(x, y, p):
    w = 0
    for i in range(len(x)):
        w += (abs(x[i]-y[i]))**2
    return w**(1/p)

def Maximum(x, y): 
    tab = []
    for i in range(len(x)):
        tab.append(abs(x[i]-y[i]))
    return max(tab)


distan = {
    "Euklidean": lambda x, y: Minkowski(x, y, 2),
    "Minkowski": lambda x, y, p: Minkowski(x, y, p),
    "Manhattan": lambda x, y: Minkowski(x, y, 1),
    "Maximum": lambda x, y: Maximum(x, y)
}