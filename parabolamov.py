from matplotlib import pyplot as plt
from numpy import (uint8, fromstring as np_fromstring)
from moviepy.editor import (ImageClip, concatenate_videoclips)

SIZE = 100

def plot(points):
    """Plot a list of (x, y) points to a matplotlib.pyplot.figure"""
    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.tick_params(labelbottom='off', labelleft='off')
    ax.plot([p[0] for p in points], [p[1] for p in points], '-o')
    ax.set_xlim(-SIZE, SIZE)
    ax.set_ylim(0, SIZE**2)
    fig.canvas.draw()
    return fig

def figures():
    # Generate the points on a parabola
    parabolaPoints = [(x, x**2) for x in range(-SIZE, SIZE+1)]
    for i in range(0, SIZE*2+1):
        figure = plot(parabolaPoints[:i+1])
        yield figure

def fig_to_rgb(fig):
    """Convert the plot to a numpy array of 24-bit RGB data"""
    data = np_fromstring(fig.canvas.tostring_rgb(), dtype=uint8, sep='')
    retval = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return retval

def fig_to_clip(fig, duration=1):
    """Render a matplotlib.pyplot.figure to an ImageClip of given duration"""
    data = fig_to_rgb(fig)

    # Add the plot to a movie-clip "image"
    retval = ImageClip(data)
    retval.duration = duration
    retval.fps = 60
    return retval

if __name__ == '__main__':
    clips = [fig_to_clip(fig, 1) for fig in figures()]
    composite = concatenate_videoclips(clips)
    composite.write_videofile('foo.mp4')
