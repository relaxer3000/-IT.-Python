# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, razd1 = ','):
    list_1 = str_1.split(razd1)
    list_2 = str_2.split(razd1)
    i = list(set(list_1).intersection(list_2))
    i.sort()
    return i
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
razdelitel = '|'
# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, razdelitel)