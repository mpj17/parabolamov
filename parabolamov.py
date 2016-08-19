from matplotlib import pyplot as plt
import numpy as np
from moviepy.editor import (ImageClip, concatenate_videoclips)

def plot(points):
    """Plot a list of (x, y) a figure"""
    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot([p[0] for p in points], [p[1] for p in points], '-o')
    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 100**2)
    fig.canvas.draw()
    return fig

def fig_to_rgb(fig):
    # Convert the plot to 24-bit RGB data (0-255, 0-255, 0-255)
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
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

# Generate the points on a parabola
parabolaPoints = [(x, x**2) for x in range(-100, 101)]

figures = [plot(parabolaPoints[:l]) for l in
           range(1, len(parabolaPoints))]
clips = [fig_to_clip(fig, 0.1) for fig in figures]
figures = None
composite = concatenate_videoclips(clips)
# Write the clip to a file
composite.write_videofile('foo.mp4')
