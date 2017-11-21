import math
import threading

from saot.visualizer import Visualizer

if __name__ == '__main__':
    vis = Visualizer(["apple", "banana", "orange", "overall"])
    for i in range(100):
        vis.add_data("apple", i, i)
        vis.add_data("banana", i, i * i)
        vis.add_data("orange", i, math.sqrt(i))
        vis.add_data("overall", i, i, 0)
        vis.add_data("overall", i, i * i, 1)
        vis.add_data("overall", i, math.sqrt(i), 2)
        threading._sleep(0.1)
