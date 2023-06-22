# https://stackoverflow.com/questions/472000/usage-of-slots
"""
    - Faster attribute access.
    - Storing value references in slots instead of __dict__ (space savings in memory.)
    - The special attribute __slots__ allows you to explicitly state which instance attributes you expect 
        your object instances to have, with the expected results: 
"""

class SensorReading:
    __slots__ = ['id', 'value']

    def __init__(self, id:int, value:str) -> None:
        self.id = id
        self.value = value
        # self.text = "text "+ value 

    def start_reading(self):
        # self.read = "sdfs"  # it does not allow variable which is not defined in slot's
        pass

sr = SensorReading(3, "Trinath")
sr.start_reading()