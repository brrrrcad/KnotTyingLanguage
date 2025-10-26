from ktl import *
from main import R1
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

def test_figure_8_01():
    R = Rope()

    t, c1, c2 = pturn(R.w)
    c4, c3 = pcross(R.w, R.before(c1))
    p = ppass(R.w, t)

    assert_location_sublist(R, [c3, c1, c2, c4, p])

def test_reef_01():
    R1 = Rope()
    R2 = Rope()

    l1, p1 = ploop(R2.w, R1.w)
    l2, p2 = ploop(R1.w, R2.s)
    l3, p3 = nloop(R1.w, R2.w)
    p4 = npass(R1.w, l1)

    assert_location_sublist(R1, [p1, l2.loc1, l2.loc2, l3.loc1, l3.loc2, p4])
    assert_location_sublist(R2, [p2, l1.loc1, l1.loc2, p3])

def test_sheet_bend_01():
    R1 = Rope()
    R2 = Rope()
    
    l1, p1 = ploop(R2.w, R1.w)
    l2, p2 = ploop(R1.w, R2.w)
    l3, p3 = nloop(R1.w, R2.s)
    c2, c1 = ncross(R1.w, R1.between(p1, l2))
    c3, c4 = pcross(R1.w, R2.between(l1, p2))

    assert_location_sublist(R1, [p1, c1, l2.loc1, l2.loc2, l3.loc1, l3.loc2, c2, c3])
    assert_location_sublist(R2, [p3, l1.loc1, l1.loc2, c4, p2])

def test_evil_sheet_bend_01():
    R1 = Rope()
    R2 = Rope()
    
    l1, p1 = ploop(R2.w, R1.w)
    l2, p2 = ploop(R1.w, R2.s)
    l3, p3 = nloop(R1.w, R2.w)
    c2, c1 = pcross(R1.w, R1.between(p1, l2))
    c3, c4 = pcross(R1.w, R2.between(p2, l1))

    assert_location_sublist(R1, [p1, c1, l2.loc1, l2.loc2, l3.loc1, l3.loc2, c2, c3])
    assert_location_sublist(R2, [p2, c4, l1.loc1, l1.loc2, p3 ])







