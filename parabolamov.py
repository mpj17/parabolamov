from matplotlib import pyplot as plt
import numpy as np
from moviepy.editor import (ImageClip, concatenate_videoclips)


# Generate the points on a parabola
parabolaPoints = [(x, x**2) for x in range(-100, 101)]

def points_to_image(points, duration=1):
    """Plot a list of (x, y) points to an ImageClip of given duration"""
    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot([p[0] for p in points], [p[1] for p in points], '-o')
    ax.set_xlim(-100, 100)
    ax.set_ylim(0, 100**2)
    fig.canvas.draw()
    
    # Convert the plot to 24-bit RGB data (0-255, 0-255, 0-255)
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # Add the plot to a movie-clip "image"
    retval = ImageClip(data)
    retval.duration = duration
    retval.fps = 60
    return retval

clips = [points_to_image(parabolaPoints[:l], 0.1) for l in
         range(1, len(parabolaPoints))]
composite = concatenate_videoclips(clips)
# Write the clip to a file
composite.write_videofile('foo.mp4')
