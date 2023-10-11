list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
players_count = len(list_players)  # Всего людей
players_count_in_team = players_count // 2  # Количество человек в команде
first_team = list_players[:players_count_in_team]
second_team = list_players[players_count_in_team:]
print(first_team)
print(second_team)
# TODO Разделите участников на две команды
