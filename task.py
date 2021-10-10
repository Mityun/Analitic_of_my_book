def check_wrong_word(key_word):
    with open('file', 'r') as file:
        text = file.readlines()
        for i in text:
            if key_word in i.lower():
                print("Надо менять!!")
                print('Line:', text.index(i), '\n', i)

check_wrong_word('ранг')



