marks = [77,97,32,96,42,64,85,55,39]

# map()

def grade(marks):
    if marks >= 95:
        return 'O'
    elif 81 < marks <= 94:
        return 'A+'
    elif 71 <= marks <= 80:
        return 'A'
    elif 58 <= marks <= 80:
        return 'B'
    elif 47 <= marks <= 57:
        return 'C'
    elif 40 <= marks <= 46:
        return 'D'
    else:
        return 'E'
    
grades = map(grade,marks)
print("Exam Scores: ",marks)
print("Grades: ",next(grades))
print("Grades: ",list(grades))

# filter()

def failing(score):
    return score < 40

result = filter(failing,marks)
print("failing Score: ", list(result))
