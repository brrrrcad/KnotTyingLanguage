import pytest
from ktl import *
from .utils import *

def test_outer_bowline_01():
    R = Rope()

    t, c1, c2 = pturn(R.w)
    p1 = ppass(R.w, t)
    l, p2 = ploop(R.w, R.s)
    p3 = npass(R.w, t)

    R.equalize()
    assert_location_sublist(R, [p2, c1, c2, p1, l.start, l.end, p3])

def test_sheet_bend_01():
    R1 = Rope()
    R2 = Rope()

    t, c1, c2 = nturn(R1.w)
    p1 = npass(R2.w, t)
    l, p2 = ploop(R2.w, R1.s)
    p3 = ppass(R2.w, t)

    assert_location_sublist(R1, [p2, c1, c2])
    assert_location_sublist(R2, [p1, l.start, l.end, p3])
