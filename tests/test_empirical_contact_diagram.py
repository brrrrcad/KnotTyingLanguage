from geometry import *
import numpy as np

def test_contact_diagram_01():
    r_raw = read_rope_file("data/bowline_outer.csv")
    assert len(r_raw) > 0
    r = resample_rope(r_raw, 300)
    assert len(r) == 300
    distances = get_distance_matrix(r, diameter=1, epsilon=0.1)
    assert distances.shape == (300, 300)
    assert (distances > 0).sum() > 0
    assert (distances <= 0).sum() > 0

def test_polarity_diartgam_01():
    r_raw = read_rope_file("data/bowline_outer.csv")
    r = resample_rope(r_raw, 300)
    polarity_matrix, _ = get_polarity_matrices(r)
    assert polarity_matrix.shape == (300, 300)