#!/usr/bin/env python3
from matplotlib import pyplot as plt
from numpy import (uint8, fromstring as np_fromstring)
from moviepy.editor import (ImageClip, concatenate_videoclips)

SIZE = 100  # The size of the x-axis of the parabola plot: [-SIZE, SIZE]


def plot(points):
    """Plot a list of (x, y) points to a matplotlib.pyplot.figure"""
    # The actual dimensions of the movie are determined by the
    # size of the figure
    retval = plt.figure()
    ax = retval.add_subplot(1, 1, 1)
    # The labels on the tic-marks are distracting.
    ax.tick_params(labelbottom='off', labelleft='off')
    # Plot with lines between the dots.
    ax.plot([p[0] for p in points], [p[1] for p in points], '-o')
    # The x and y axis should be the same for all plots
    ax.set_xlim(-SIZE, SIZE)
    ax.set_ylim(0, SIZE**2)
    retval.canvas.draw()  # Render it, so we can get the RGB data later
    return retval


def figures():
    '''Generate the parabola figures'''
    # Lots of ``+1`` here because of how Python treats ranges.
    parabolaPoints = [(x, x**2) for x in range(-SIZE, SIZE+1)]
    for i in range(0, SIZE*2+1):
        figure = plot(parabolaPoints[:i+1])
        yield figure


def fig_to_rgb(fig):
    """Convert the plot to a numpy array of 24-bit RGB data"""
    # Thanks to Joe Kington on Stack Overflow
    # <http://stackoverflow.com/questions/7821518/matplotlib-save-plot-to-numpy-array>
    data = np_fromstring(fig.canvas.tostring_rgb(), dtype=uint8, sep='')
    retval = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return retval


def fig_to_clip(fig, duration=1):
    """Render a matplotlib.pyplot.figure to a
    ``moviepy.editor.ImageClip`` of given duration (in seconds)"""
    data = fig_to_rgb(fig)
    # Add the plot to a movie-clip "image"
    retval = ImageClip(data)
    retval.duration = duration
    retval.fps = 60  # Needlessly high
    return retval

if __name__ == '__main__':
    clips = [fig_to_clip(fig, duration=0.1) for fig in figures()]
    composite = concatenate_videoclips(clips)
    composite.write_videofile('foo.mp4')
