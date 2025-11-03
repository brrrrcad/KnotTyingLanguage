import numpy as np
from scipy.ndimage import label


def get_interactions(distances):
    contact = distances <= 0
    labelled_interactions, num_interactions = label(contact)
    interactions = []
    for interaction_id in range(1, num_interactions + 1):
        interaction_indices = np.argwhere(labelled_interactions == interaction_id)
        if (0,0) in interaction_indices:
            continue  # Skip diagonal line
        if interaction_indices[0][0] > interaction_indices[0][1]:
            continue  # Skip interactions below the diagonal
        print(f"Interaction length:{len(interaction_indices)}")
        interactions.append(interaction_indices)
    return interactions