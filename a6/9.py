exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}

user_input = int(input())

final_dict = {}

for key, value in exam_marks.items():
    if user_input <= exam_marks[key]:
        final_dict[key] = exam_marks[key]

print(final_dict)