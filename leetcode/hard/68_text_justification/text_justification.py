from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        spaces = []
        current_line = ""
        for word in words:
            current_line = current_line.lstrip()
            if len(current_line) + len(word) + 1 <= maxWidth:
                current_line += " " + word
            else:
                lines.append(current_line)
                spaces.append(lines[-1].count(" "))
                current_line = word
        lines.append(current_line.lstrip())
        spaces.append(lines[-1].count(" "))
        result = []
        for i in range(len(lines) - 1):
            number_of_spaces_needed = maxWidth - \
                len(lines[i].replace(" ", ""))
            number_of_places_for_spaces = max(spaces[i], 1)
            spaces_per_word = number_of_spaces_needed // number_of_places_for_spaces
            extra_spaces = number_of_spaces_needed % number_of_places_for_spaces
            string = ""
            for j in range(len(lines[i])):
                if lines[i][j] == " ":
                    string += " " * spaces_per_word
                    if extra_spaces > 0:
                        string += " "
                        extra_spaces -= 1
                else:
                    string += lines[i][j]
            result.append(string)
        result.append(lines[-1])
        for i in range(len(lines)):
            number_of_spaces_needed = maxWidth - len(result[i])
            result[i] += " " * number_of_spaces_needed
        return filter(lambda x: x != " " * len(x), result)


sol = Solution().fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16)
for line in sol:
    print(line + ";")
print()
sol = Solution().fullJustify(
    ["What", "must", "be", "acknowledgment", "shall", "be"], 16)
for line in sol:
    print(line + ";")
sol = Solution().fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
for line in sol:
    print(line + ";")
print()
sol = Solution().fullJustify(
    ["Listen", "to", "many,", "speak", "to", "a", "few."], 6)
for line in sol:
    print(line + ";")
print()
sol = Solution().fullJustify(
    ["a"], 2)
for line in sol:
    print(line + ";")
print()
print()
sol = Solution().fullJustify(
    ["a", "b", "c", "d", "e"], 3)
for line in sol:
    print(line + ";")
print()
