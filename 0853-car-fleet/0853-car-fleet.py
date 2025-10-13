class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = [[p, s] for p, s in zip(position, speed)]
        positionSpeed.sort(reverse=True)
        fleets = []
        
        for p, s in positionSpeed:
            fleets.append((target - p) / s)
            if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        
        return len(fleets)