class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballColor = {}
        colorCount = {}
        result = []

        for i in queries:
            if i[0] in ballColor:
                colorCount[ballColor[i[0]]] -= 1
                if colorCount[ballColor[i[0]]] == 0:
                    colorCount.pop(ballColor[i[0]])
            
            ballColor[i[0]] = i[1]
            colorCount[i[1]] = colorCount.get(i[1], 0) + 1
            
            result.append(len(colorCount))
        
        return result