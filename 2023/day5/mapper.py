from typing import List

class MapComponent:
    def __init__(self, sourceStart: int, destinationStart: int, range: int):
        self.sourceStart = sourceStart
        self.destinationStart = destinationStart
        self.range = range

class Mapper:
    def __init__(self):
        self.mapComponents: List[MapComponent] = []
    
    def Map(self, input: int):
        for component in self.mapComponents:
            if input >= component.sourceStart and input < component.sourceStart + component.range:
                return component.destinationStart + (input - component.sourceStart)
        
        return input