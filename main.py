from geometry import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RESOLUTION = 300
DIAMETER = 1
EPSILON = 0.1


df = read_rope_file("data/bowline_outer.csv")

result_df = resample_rope(df, RESOLUTION)

distances = get_distance_matrix(result_df, diameter=DIAMETER, epsilon=EPSILON)

#max_distances = np.nanmax(distances)
# Mask negative distances
clipped_distances = distances.copy()
clipped_distances[clipped_distances <= 0] = np.nan


# Plot Diagram
length = df['CumulativeLength'].iloc[-1]
extent=[0, length/DIAMETER, length/DIAMETER, 0]
plt.imshow(clipped_distances, cmap='viridis_r', interpolation='nearest', origin='upper', extent=extent)
plt.xlabel('Point 2 [Diams]')
plt.ylabel('Point 1 [Diams]')
plt.colorbar().set_label('Distance [Diams]')
#levels = range(0, int(np.floor(max_distances)))
#plt.contour(distances, levels=[0,1,2,3,4,5], colors='black', origin='upper', extent=extent)
#plt.contour(distances, levels=[0], colors='red', origin='upper', extent=extent)
plt.title('Empirical Contact Diagram')
plt.gca().set_facecolor('black')

plt.show()

