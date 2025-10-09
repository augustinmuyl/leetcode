class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []

        for i, v in enumerate(path.split("/")):
            if v == "..":
                if dirs:
                    dirs.pop()
            elif v not in " .":
                dirs.append(v)
                    
        return "".join("/" + i for i in dirs) if dirs else "/"