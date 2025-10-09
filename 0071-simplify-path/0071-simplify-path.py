class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = ["root"]
        dir_indexes = []
        curr_dir = ""

        for i, v in enumerate(path):
            if v == "/" and len(dir_indexes) <= 1:
                dir_indexes.append(i)
            
            if len(dir_indexes) > 1 or i == len(path) - 1:
                if i == len(path) - 1 and len(dir_indexes) <= 1:
                    curr_dir = path[dir_indexes[0] + 1:]
                else:
                    curr_dir = path[dir_indexes[0] + 1: dir_indexes[1]]

                if curr_dir == ".":
                    pass
                elif curr_dir == "..":
                    if dirs[-1] != "root":
                        dirs.pop()
                elif curr_dir != "":
                    dirs.append(curr_dir)
                
                if i != len(path) - 1:
                    dir_indexes = [dir_indexes[1]]
                    
        return "".join("/" + i for i in dirs[1:]) if len(dirs) > 1 else "/"