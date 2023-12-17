list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
k = int(len(list_players) / 2)
new_list_1 = list_players[:k]
new_list_2 = list_players[k:]
print(new_list_1)
print(new_list_2)
