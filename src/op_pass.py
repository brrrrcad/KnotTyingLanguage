from .rope import Location, Section



def _pass(loc:Location, sec:Section, direction:bool):
    # TODO: Establish relation between loc_p
    rope = loc.rope
    p = Location(rope, loc._get_location())
    rope._add_location(p)
    return p

def ppass(loc:Location, sec:Section):
    return _pass(loc, sec, True)

def npass(loc:Location, sec:Section):
    return _pass(loc, sec, False)