def pangrams(s):
    return "pangram" if len(set(list(s.replace(" ", "").lower()))) == 26 else "not pangram"
