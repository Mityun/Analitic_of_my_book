print("Сразись с физиком за оценку!")
print("что ты сделаеш первым ходом: 1)формула  2)задача  3)можно выйти?")
a = input()
if a == "1":
    print("Ты говоришь ему формулу теплоты и приближаешься к пятерке")
elif a == "2":
    print("Ты успешно решаешь задачу по тепловому неравенству и все ближе к пятерке")
elif a == "3":
    print("БАН ТЕБЕ и 2 в журнал(((")
elif a != "1" and a != "2" and a != "3":
    print("Такого нет в ответах!")
print("Что дальше? : 1)спор по условию 2) подстановка в формуле 3) можно выйти?")
b = input()
if a == "1" and b == "1":
    print("Ты не понял условие и из-за этого тебе поставили не пять, а четыре")
elif a == "1" and b == "2":
    print("Отлично, ты решаешь очередную задачу и тебе ставят ПЯТЬ!!!")
elif a == "1" and b == "3":
    print("Да, выйди. Ты потерял свою возможность ответить еще и не получил ничего")
elif a == "2" and b == "1":
    print("в результате спора ты оказываешься прав и учитель хвалит тебя за внимательность, в итоге ты получаешь ПЯТЬ")
elif a == "2" and b == "2":
    print("Пятерка у тебя в кармане)))")
elif a == "2" and b == "3":
    print("ТЫ НЕ МОГ ПОТЕРПЕТЬ??? ТЕПЕРЬ НЕ ПОСТАВЯТ 5(((")
elif a == "3" and b == "1":
    print("НЕ, ну это ГГ...")
elif a == "3" and b == "2":
    print("Молодец, и в туалет сгонял и 4 получил!")
elif a == "3" and b == "3":
    print("Я конечно понимаю, что страшно, но не на столько же...")
elif a != "1" and a != "2" and a != "3" and b != "1" and b != "2" and b != "3":
    print("Такого нет в ответах!")
