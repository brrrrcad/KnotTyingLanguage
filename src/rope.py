



class LocationBase():
    def __init__(self, rope):
        self.rope = rope

    def get_location(self):
        raise NotImplementedError()

class WorkingEnd(LocationBase):
    def get_location(self):
        return (self.rope.get_largest_location() + 1) / 2

class Location(LocationBase):
    def __init__(self, rope, lacation:float):
        super().__init__(rope)
        self.lacation = lacation

    def get_location(self):
        return self.lacation
    

class Rope():
    def __init__(self):
        self.w = WorkingEnd(self)
        self.s = Location(self, 0)
        self.locations = [self.s]
    
    def get_largest_location(self):
        return max([loc.get_location() for loc in self.locations])