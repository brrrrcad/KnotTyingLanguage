import numpy as np
from scipy.ndimage import label
import pandas as pd


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
        interactions.append(interaction_indices)
    return interactions

def analyze_interactions(rope, distances, c_polarity, t_polarity):
    interacts = get_interactions(distances)
    rows = []
    for interact in interacts:
        c = np.mean(c_polarity[interact],where=np.isfinite(c_polarity[interact])) #TODO: Solve NaNs in c_polarity
        t = np.mean(t_polarity[interact],where=np.isfinite(t_polarity[interact])) #TODO: Solve NaNs in t_polarity
        polarity = np.sign(c) if np.abs(c)>np.abs(t) else np.sign(t)
        kind = "cross" if np.abs(c)>np.abs(t) else "trace" 
        lis = rope.iloc[[i[0] for i in interact], rope.columns.get_loc("CumulativeLength")]
        ljs = rope.iloc[[i[1] for i in interact], rope.columns.get_loc("CumulativeLength")]
        li = np.mean(lis)
        lj = np.mean(ljs)
        row = {
            "Indices":interact,
            "Size":len(interact),
            "li": li,
            "lj": lj,
            "c": c,
            "t": t,
            "polarity":polarity,
            "kind":kind,
        }
        rows.append(row)
    return pd.DataFrame(rows)