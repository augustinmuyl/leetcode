class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballColor = {}
        colorCount = {}
        result = []

        for x, y in queries:
            oldColor = ballColor.get(x)
            if oldColor != y:
                if oldColor is not None:
                    colorCount[oldColor] -= 1
                    if colorCount[oldColor] == 0:
                        del colorCount[oldColor]
                
                ballColor[x] = y
                colorCount[y] = colorCount.get(y, 0) + 1
            
            result.append(len(colorCount))
        
        return result