
course_total = 0

labs = float(input("How many labs have been completed sir?"))
if labs > 6:
    labs = 6
labs_weight = 0.20

course_total += labs / 6 * labs_weight

quizzes = float(input("How many quizzes or in-class activitie have been completed Mr. Teacher?"))
if quizzes > 6:
    quizzes = 6
quizzes_weight = 0.15

course_total += #entergirl

final_grade = float(input("give me your final grade"))
final_weight = 0.18

course_total += final_grade * final_weight


