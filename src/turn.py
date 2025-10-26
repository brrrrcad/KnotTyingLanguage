from .rope import Location, Section

def _turn(loc:Location, direction:bool):
    rope = loc.rope
    loc2 = Location(rope, loc._get_location())
    rope._add_location(loc2)
    loc1 = rope.before(loc2)
    rope._add_location(loc1)    
    section = Section(loc1, loc2)
    rope._add_section(section)
    return section, loc1, loc2

def pturn(loc2:Location):
    return _turn(loc2, True)

def nturn(loc2:Location):
    return _turn(loc2, False)
    
