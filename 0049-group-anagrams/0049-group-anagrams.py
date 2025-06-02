class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        B = []

        for i in strs:
            s = ''.join(sorted(i))
            if s not in A:
                A.update({s: [i]})
            elif s in A:
                x = A.get(s)
                x.append(i)
                A.update({s: x})

        for i in A:
            B.append(A.get(i))
        
        return B
        