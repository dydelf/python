import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep running the program until break
while True:
    # make a random walk and plt the points
    rw = RandomWalk(10000)
    rw.fill_walk()
    # set the size of ploting window
    plt.figure(figsize=(10, 6))
    # set the parameters of the plot
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Reds, edgecolor='none', s=10)
    # emphasize th starting and end point
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolor='none', s=100)
    # remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    # repeat the random walk and plotting
    keep_running = input("Do you want to keep running? y/n")
    if keep_running == 'n':
        break
