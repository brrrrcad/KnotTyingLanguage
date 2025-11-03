from geometry import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RESOLUTION = 300
DIAMETER = 1
EPSILON = 0.1


rope = read_rope("data/bowline_outer.csv", RESOLUTION)


#draw_ecd(result_df, diameter=DIAMETER, epsilon=EPSILON)

#draw_epd(result_df, diameter=DIAMETER, epsilon=EPSILON)

distances = get_distance_matrix(rope, diameter=DIAMETER, epsilon=EPSILON)
c_polarity, t_polarity = get_polarity_matrices(rope)
df_rows = analyze_interactions(rope, distances, c_polarity, t_polarity)
print(df_rows)


