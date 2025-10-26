from .rope import Location, Section

def _turn(loc:Location, direction:bool):
    # TODO: Establish relation 
    rope = loc.rope
    c2 = Location(rope, loc._get_location())
    rope._add_location(c2)
    c1 = rope.before(c2)
    rope._add_location(c1)    
    t = Section(c1, c2)
    rope._add_section(t)
    return t, c1, c2

def pturn(loc2:Location):
    return _turn(loc2, True)

def nturn(loc2:Location):
    return _turn(loc2, False)
    
