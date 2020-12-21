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