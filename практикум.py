FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def print_friends_count(query, friends_count):

    if query == 'Сколько у меня друзей?':
        if friends_count == 1:
            print('У тебя 1 друг')
        elif 2 <= friends_count <= 4:
            print('У тебя ' + str(friends_count) + ' друга')
        elif friends_count >= 5:
            print('У тебя ' + str(friends_count) + ' друзей')
    else:
        print('<неизвестный запрос>')


def process_query():
    print("Привет, я Анфиса!")
    count = len(FRIENDS)
    print_friends_count(count)
    query = input()

