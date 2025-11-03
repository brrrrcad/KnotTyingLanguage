from geometry import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RESOLUTION = 300
DIAMETER = 1
EPSILON = 0.1


df = read_rope_file("data/bowline_inner.csv")

result_df = resample_rope(df, RESOLUTION)

#draw_ecd(result_df, diameter=DIAMETER, epsilon=EPSILON)

draw_epd(result_df, diameter=DIAMETER, epsilon=EPSILON)


