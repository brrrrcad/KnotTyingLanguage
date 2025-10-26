from .rope import Location


def _cross(loc_a, loc_b, direction:bool):
    # TODO: add relation
    rope_a = loc_a.rope
    ca = Location(rope_a, loc_a._get_location())
    rope_a._add_location(ca)

    rope_b = loc_b.rope
    cb = Location(rope_b, loc_b._get_location())
    rope_b._add_location(cb)
    return ca, cb

def pcross(loc_a:Location, loc_b:Location):
    return _cross(loc_a, loc_b, True)

def ncross(loc_a:Location, loc_b:Location):
    return _cross(loc_a, loc_b, False)