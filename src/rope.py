
LOC_MAX = 1
LOC_MIN = 0


class LocationBase():
    def __init__(self, rope):
        self.rope = rope

    def _get_location(self):
        raise NotImplementedError()
    
    

class WorkingEnd(LocationBase):
    def _get_location(self):
        return (self.rope._get_largest_location() + LOC_MAX) / 2
    
class StandingEnd(LocationBase):
    def _get_location(self):
        return (self.rope._get_smallest_location() + LOC_MIN) / 2

class Location(LocationBase):
    def __init__(self, rope, location:float):
        super().__init__(rope)
        self.location = location

    def _get_location(self):
        return self.location
    
class Section:
    def __init__(self, loc1:Location, loc2:Location):
        assert loc1.rope == loc2.rope
        self.loc1 = loc1
        self.loc2 = loc2

        
    

class Rope():
    def __init__(self):
        self.w = WorkingEnd(self)
        self.s = StandingEnd(self)
        self.loc_placeholder = Location(self, (LOC_MAX + LOC_MIN) / 2)
        self.locations = [self.loc_placeholder]
        self.sections = set()
    
    def _get_largest_location(self):
        return max([loc._get_location() for loc in self.locations])
    
    def _get_smallest_location(self):
        return min([loc._get_location() for loc in self.locations])
    
    def _add_location(self, loc:Location):
        self.locations.append(loc)
        self.locations.sort(key=lambda l: l._get_location())

    def _add_section(self, section:Section):
        self.sections.add(section)

    ### USER METHODS ###

    def before(self, location):
        loc2_value = location._get_location()
        loc1_value = max(filter(lambda l: l._get_location() < loc2_value, self.locations))._get_location()
        new_loc = Location(self, (loc1_value + loc2_value) / 2)
        return new_loc