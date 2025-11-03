import numpy as np
import matplotlib.pyplot as plt
from .utils import split_param

def get_distance_matrix(rope, diameter, epsilon=0.1):

    # Usage with two ropes or one rope
    rope1, rope2 = split_param(rope)
    diameter1, diameter2 = split_param(diameter)

    # Calculation of distance matrix
    distances = np.zeros((len(rope1), len(rope2)))
    for i in range(len(rope1)):
        for j in range(len(rope2)):
            print(f"Calculating distances for point {np.round(100*(i+1)/len(rope1),1)}%", end='\r')
            dx = rope1['x'].iloc[i] - rope2['x'].iloc[j]
            dy = rope1['y'].iloc[i] - rope2['y'].iloc[j]
            dz = rope1['z'].iloc[i] - rope2['z'].iloc[j]
            distances[i,j] = (dx*dx + dy*dy + dz*dz)**0.5 - (diameter1 + diameter2)*(1+epsilon)/2
    return distances




def draw_ecd(rope, diameter, epsilon=0.1):
    

    distances = get_distance_matrix(rope, diameter, epsilon)
    rope1, rope2 = split_param(rope)
    diameter1, diameter2 = split_param(diameter)
    length1 = rope1['CumulativeLength'].iloc[-1]
    length2 = rope2['CumulativeLength'].iloc[-1]

    # Mask negative distances
    clipped_distances = distances.copy()
    clipped_distances[clipped_distances <= 0] = np.nan

    # Plot Diagram
    extent=[0, length2/diameter2, length1/diameter1, 0]
    plt.imshow(clipped_distances, cmap='viridis_r', interpolation='nearest', origin='upper', extent=extent)
    plt.xlabel('Point 2 [Diams]')
    plt.ylabel('Point 1 [Diams]')
    plt.colorbar().set_label('Distance [Diams]')
    plt.title('Empirical Contact Diagram')
    plt.gca().set_facecolor('black')
    plt.show()