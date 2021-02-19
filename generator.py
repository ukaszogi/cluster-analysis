import random as rd
import json

def random2D(name = "rand_points.json", subX = 1, supX = 100, subY = 1, supY = 100, c = 100):
    """Generates JSON file with random set of points on a 2D space.

    Args:
        name (str, optional): name of the json file. Defaults to "rand_points.json".
        subX (int, optional): lower bound of x. Defaults to 1.
        supX (int, optional): upper bound of x. Defaults to 100.
        subY (int, optional): lower bound of y. Defaults to 1.
        supY (int, optional): upper bound of y. Defaults to 100.
        c (int, optional): number of points. Defaults to 100.
    """
    points = []
    for _ in range(c):
        x = rd.random()*(supX-subX)+subX
        y = rd.random()*(supY-subY)+subY
        points.append((x, y))
    file = open(name, 'w')
    file.write(json.dumps(points, indent=4))    
    file.close()

def clusters2D():
    pass

random2D()