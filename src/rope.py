



class LocationBase():
    def __init__(self, rope):
        self.rope = rope

    def _get_location(self):
        raise NotImplementedError()

class WorkingEnd(LocationBase):
    def _get_location(self):
        return (self.rope._get_largest_location() + 1) / 2
    
class StandingEnd(LocationBase):
    def _get_location(self):
        return (self.rope._get_smallest_location()) / 2

class Location(LocationBase):
    def __init__(self, rope, lacation:float):
        super().__init__(rope)
        self.lacation = lacation

    def _get_location(self):
        return self.lacation
    

class Rope():
    def __init__(self):
        self.w = WorkingEnd(self)
        self.s = StandingEnd(self)
        self.loc_placeholder = Location(self, 0.5)
        self.locations = [self.loc_placeholder]
    
    def _get_largest_location(self):
        return max([loc._get_location() for loc in self.locations])
    
    def _get_smallest_location(self):
        return min([loc._get_location() for loc in self.locations])