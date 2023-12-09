from typing import List

class SeedRange:
    def __init__(self, start: int, range: int):
        self.start = start
        self.range = range

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

    def MapRange(self, inputRanges: List[SeedRange]):
        ret = []
        for inputRange in inputRanges:
            start = inputRange.start
            range = inputRange.range
            startRange = None
            for component in self.mapComponents:
                if start >= component.sourceStart and start < component.sourceStart + component.range:
                    startRange = component
                    break
            
            if startRange is None:
                componentStart = start
                self.mapComponents.sort(key=lambda c: c.sourceStart)
                for mapComponent in self.mapComponents:
                    if mapComponent.sourceStart > componentStart:
                        startRange = MapComponent(componentStart, componentStart, mapComponent.sourceStart - componentStart)
                        break
                if startRange is None:
                    startRange = MapComponent(start, start, range)

            if start + range <= startRange.sourceStart + startRange.range:
                ret.append(SeedRange(startRange.destinationStart + (start - startRange.sourceStart), range))
            else:
                rangeMapped = startRange.sourceStart + startRange.range - start
                ret.append(SeedRange(startRange.destinationStart + (start - startRange.sourceStart), rangeMapped))
                ret.extend(self.MapRange([SeedRange(startRange.sourceStart + startRange.range, range - rangeMapped)]))
        
        return ret