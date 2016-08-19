from matplotlib import pyplot as plt
import numpy as np
from moviepy.editor import ImageClip


# Generate the points on a parabola
points = [(x, x**2) for x in range(-10, 10)]

# Plot the points
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter([p[0] for p in points], [p[1] for p in points])
fig.canvas.draw()

# Convert the plot to 24-bit RGB data (0-255, 0-255, 0-255)
data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

# Add the plot to a movie-clip "image"
i = ImageClip(data)
i.duration = 5
i.fps = 60

# Write the clip to a file
i.write_gif('foo.gif')
