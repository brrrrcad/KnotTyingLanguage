from ktl import Rope, Location

def assert_location_sublist(rope:Rope, reference:list[Location]):
    locations = [loc for loc in rope.locations if loc in reference]
    assert locations == reference