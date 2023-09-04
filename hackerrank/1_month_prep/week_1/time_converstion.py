def timeConversion(s):
    is_pm = s[-2:] == "PM"
    hour = int(s[:2])
    if hour == 12:
        hour = 0
    if is_pm:
        hour += 12
    return str(f'{hour:02}') + s[2:-2]
