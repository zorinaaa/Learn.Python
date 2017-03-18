school = [
        {'school_class': '5а', 'scores': [3,3,3,3,4,3,4]},
        {'school_class': '6б', 'scores': [4,5,5,5,4,2,5]},
        {'school_class': '7в', 'scores': [3,3,2,5,5,3,4]},
        {'school_class': '8г', 'scores': [5,5,3,2,3,4,5]},
        {'school_class': '9д', 'scores': [5,4,5,5,4,5,5]},
        {'school_class': '10а', 'scores': [4,5,5,4,4,4,3]},
        {'school_class': '11б', 'scores': [4,4,5,5,5,5,4]},   
    ]

sum_school = 0
count_school = 0

for score in school:
    sc_list = score.get('scores')
    sch_class = score['school_class']
    print ('Оценки по классу:', sch_class)

    sum_class = 0

    for elem in sc_list:
        sum_class += elem
    arithm_class = sum_class / len(sc_list)
    print('Средний балл:', round(arithm_class))

    sum_school += sum_class

    for ind in sc_list:
        count_school += 1

arithm_school = int(sum_school / count_school)
print('Среднний балл по школе:', arithm_school)
