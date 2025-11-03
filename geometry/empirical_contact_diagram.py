import numpy as np
import pandas as pd

def get_distance_matrix(rope, diameter, epsilon=0.1):

    # Usage with two ropes or one rope
    if isinstance(rope, tuple) and len(rope) == 2:
        rope1 = rope[0]
        rope2 = rope[1]
        if isinstance(diameter, tuple) and len(diameter) == 2:
            diameter1 = diameter[0]
            diameter2 = diameter[1]
        else:
            diameter1 = diameter2 = diameter
    else:
        rope1 = rope2 = rope
        diameter1 = diameter2 = diameter

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