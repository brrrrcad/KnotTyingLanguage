from .rope import Location, Section, WorkingEnd


def _loop(loc_l:Location, loc_p:Location):
    assert isinstance(loc_l, WorkingEnd) or isinstance(loc_p, WorkingEnd)
    # TODO: Establish relation between loc and sec
    rope_l = loc_l.rope
    loop_end = Location(rope_l, loc_l._get_location())
    rope_l._add_location(loop_end)
    loop_start = rope_l.before(loop_end)
    rope_l._add_location(loop_start)
    l = Section(loop_start, loop_end)
    rope_l._add_section(l)

    rope_p = loc_p.rope
    p = Location(rope_p, loc_p._get_location()) # TODO: only if not yet in rope_b.locations!
    rope_p._add_location(p)

    return l, p

def ploop(loc:Location, sec:Section):
    return _loop(loc, sec)

def nloop(loc:Location, sec:Section):
    return _loop(loc, sec)