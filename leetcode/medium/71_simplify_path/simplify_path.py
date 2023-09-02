class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = list(filter(lambda x: x != "", path.split("/")))
        result = []
        for token in tokens:
            match token:
                case "..":
                    if len(result) >= 1:
                        result.pop()
                case ".":
                    continue
                case _:
                    result.append(token)
        return "/" + "/".join(result)


print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/home//foo/"))
print(Solution().simplifyPath("/a/./b/../../c/"))
