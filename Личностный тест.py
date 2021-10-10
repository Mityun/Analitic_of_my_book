print("любишь математику?")
a = input()
print("And what about English?!")
s = input()
if (a != "Да" and a != "Нет") and (s != "Да" and s != "Нет"):
    print("Ах ты хитрожопый какой!")
elif a == "Да" and s == "Да":
    print("А ты хорош)")
elif a == "Да" and s == "Нет":
    print("я так понял ты English не speak...")
elif a == "Нет" and s == "Да":
    print("I think you need to do math more")
elif a == "Нет" and s == "Нет":
    print("Не ну это бан")

