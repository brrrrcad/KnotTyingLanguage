
from .utils import split_param
from .empirical_contact_diagram import get_distance_matrix
import numpy as np
from skimage import color
import matplotlib.pyplot as plt

def diff_coordinate(c):
    dc = c.diff().fillna(0)
    dc[0] = c[1] - c[0]
    return dc

def get_polarity_matrices(rope):
    rope1, rope2 = split_param(rope)
    dx1 = diff_coordinate(rope1['x'])
    dy1 = diff_coordinate(rope1['y'])
    dz1 = diff_coordinate(rope1['z'])
    dx2 = diff_coordinate(rope2['x'])
    dy2 = diff_coordinate(rope2['y'])
    dz2 = diff_coordinate(rope2['z'])

    c_polarity_matrix = np.zeros((len(rope1), len(rope2)))
    t_polarity_matrix = np.zeros((len(rope1), len(rope2)))

    for i in range(len(rope1)):
        print(f"Calculating polarity for point {np.round(100*(i+1)/len(rope1),1)}%", end='\r')

        delta_1 = np.array([dx1.iloc[i], dy1.iloc[i], dz1.iloc[i]])
        norm_1 = np.linalg.norm(delta_1)
        assert norm_1 >= 0
        delta_1 = delta_1 / norm_1

        for j in range(len(rope2)):
            delta_2 = np.array([dx2.iloc[j], dy2.iloc[j], dz2.iloc[j]])
            norm_2 = np.linalg.norm(delta_2)
            assert norm_2 >= 0
            delta_2 = delta_2 / norm_2 

            difference_vector = np.array([
                rope1['x'].iloc[i] - rope2['x'].iloc[j],
                rope1['y'].iloc[i] - rope2['y'].iloc[j],
                rope1['z'].iloc[i] - rope2['z'].iloc[j]
            ])
            difference_norm = np.linalg.norm(difference_vector)
            assert difference_norm >= 0
            difference_vector = difference_vector / difference_norm 


            c_polarity_matrix[i,j] = np.dot(np.cross(delta_1, delta_2), difference_vector)
            t_polarity_matrix[i,j] = np.dot(np.cross(delta_1, difference_vector), np.cross(delta_2, difference_vector))
            

    return c_polarity_matrix, t_polarity_matrix

def draw_epd(rope, diameter, epsilon=0.1):
    distance_matrix = get_distance_matrix(rope, diameter, epsilon)
    A, B = get_polarity_matrices(rope)
    L = np.ones_like(distance_matrix)
    L[distance_matrix > 0] = 0.5/(distance_matrix[distance_matrix > 0]+1)
    lab_image = np.stack([L*100, A*127, B*127], axis=-1)
    rgb_image = color.lab2rgb(lab_image)
    plt.imshow(rgb_image)
    plt.axis("off")
    plt.show()


    

    