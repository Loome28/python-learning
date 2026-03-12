def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"
print(get_grade(85))
print(get_grade(72))
print(get_grade(59))
print(get_grade(90))