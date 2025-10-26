from ktl import *
from .utils import *

def test_half_hitch_01():
    R = Rope()
    OBJ = Rope()
    l1, p1 = ploop(R.w, OBJ.somewhere())
    l2, p2 = ploop(R.w, R.s)
    c2, c1 = pcross(R.w, R.between(l1, l2))

    assert_location_sublist(R, [p2, l1.loc1, l1.loc2, c1, l2.loc1, l2.loc2, c2])

def test_clove_hitch_01():
    R = Rope()
    OBJ = Rope() 
    t1, c1, c2 = pturn(R.w)
    p1 = ppass(OBJ.w, t1)
    t2, c3, c4 = pturn(R.s)
    p2 = ppass(OBJ.w, t2)

    assert_location_sublist(R, [c3, c4, c1, c2])
    assert_location_sublist(OBJ, [p1, p2])

def test_clove_hitch_02():
    R = Rope()
    OBJ = Rope()
    l1, p1 = ploop(R.w, OBJ.somewhere())
    c2, c1 = pcross(R.w, R.before(l1))
    l2, p2 = ploop(R.w, OBJ.before(p1))
    p3 = ppass(R.w, l1)

    assert_location_sublist(R, [c1, l1.loc1, l1.loc2, c2, l2.loc1, l2.loc2, p3])
    assert_location_sublist(OBJ, [p2, p1])