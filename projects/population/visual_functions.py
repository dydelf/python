"""
Classes needed to visualise an examples of data inputted
"""

import matplotlib
matplotlib.use('tkagg')
from matplotlib import pyplot as plt


class visual():
    """ Collection of visualisation functions, plot, scatter and bar """

    def __init__(self, xaxis, yaxis, title, xlabel, ylabel):
        """ initializing attributes """
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def get_plot(self):
        """ plotting the given points """
        plt.figure(figsize=(10, 6))
        plt.plot(self.xaxis, self.yaxis, linewidth=5)
        plt.title(self.title, fontsize=24)
        plt.xlabel(self.xlabel, fontsize=14)
        plt.ylabel(self.ylabel, fontsize=14)
        plt.show()
        return plt.show()

    def get_scatter(self):
        """ getting a scatter graph """
        plt.figure(figsize=(10, 6))
        plt.scatter(self.xaxis, self.yaxis,
                    cmap=plt.cm.Reds, edgecolor='none', s=10)
        plt.show()
        return plt.show()

    def get_bar(self):
        """ getting a bar graph """
        plt.figure(figsize=(10, 6))
        plt.bar()
        plt.show()
        return plt.show()
