import Queue
import math
import threading

import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, table_names, pause_interval=0.1):
        self.pause_interval = pause_interval
        self.char = ["k+", "b*", "rx", 'go']
        self.table_names = list(set(table_names))
        self.data_queue = Queue.Queue()
        threading.Thread(target=self.figure_thread).start()

    def figure_thread(self):
        plt.ion()
        self.figures = plt.figure()
        self.table_map = {}
        num = len(self.table_names)
        w, h = self.calwh(num)
        for i in range(w):
            for j in range(h):
                idx = i * h + j
                if idx < num:
                    ax = self.figures.add_subplot(w, h, 1 + idx)
                    ax.set_xlim(0, 1)
                    ax.set_ylim(0, 1)
                    ax.set_title(self.table_names[idx])
                    self.table_map[self.table_names[idx]] = ax

        while True:
            (table, x, y, idx) = self.data_queue.get()
            ax = self.table_map[table]
            ax.set_xlim(min(x, ax.get_xlim()[0]), max(x, ax.get_xlim()[1]))
            ax.set_ylim(min(y, ax.get_ylim()[0]), max(y, ax.get_ylim()[1]))
            ax.plot(x, y, self.char[idx])
            plt.pause(self.pause_interval)

    def calwh(self, num):
        w = int(math.sqrt(num))
        if w * w == num:
            return (w, w)
        elif w * (w + 1) >= num:
            return (w, w + 1)
        else:
            return (w + 1, w + 1)

    def add_data(self, table, x, y, idx=0):
        self.data_queue.put((table, x, y, idx))
