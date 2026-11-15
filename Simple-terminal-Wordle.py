import random

wordsRU = [
    "автор", "адрес", "актер", "ангел", "арбуз", "армия", "арена", "архив", "багаж", "базар",
    "балет", "банка", "баран", "башня", "белка", "берег", "билет", "битва", "бланк", "блеск",
    "блюдо", "бокал", "бонус", "бочка", "бремя", "броня", "буква", "букет", "булка", "буфер",
    "вагон", "ванна", "ведро", "венок", "весна", "ветер", "вечер", "взвод", "видео", "вилка",
    "вишня", "вклад", "влага", "вобла", "война", "волна", "волос", "ворон", "врата", "время",
    "выбор", "вывод", "вызов", "выход", "газон", "гараж", "гений", "герой", "глава", "глина",
    "голод", "голос", "город", "горка", "гость", "грань", "грипп", "гроза", "груша", "гряда",
    "губка", "дверь", "девиз", "диван", "диета", "длина", "дождь", "домик", "доска", "драма",
    "дрова", "дрозд", "дымка", "жажда", "живот", "жизнь", "забор", "завод", "закат", "закон",
    "залив", "замок", "запах", "запас", "заряд", "затея", "зверь", "земля", "зерно", "знамя",
    "игрок", "икона", "искра", "кабан", "казак", "канал", "капля", "карта", "каюта", "квота",
    "кефир", "киоск", "класс", "клоун", "книга", "ковер", "комар", "конец", "копия", "кошка"
]
wordsEN = [
    "apple", "beach", "brain", "bread", "brush", "chair", "chest", "chord", "click", "clock",
    "cloud", "dance", "diary", "drink", "drive", "earth", "feast", "field", "flame", "floor",
    "focus", "force", "frame", "fresh", "front", "fruit", "ghost", "glass", "globe", "grade",
    "grape", "grass", "green", "group", "guard", "guess", "guide", "heart", "heavy", "horse",
    "hotel", "house", "human", "ideal", "image", "index", "input", "issue", "juice", "knife",
    "layer", "learn", "level", "light", "limit", "logic", "lunch", "magic", "major", "march",
    "match", "metal", "model", "money", "month", "motor", "mouse", "mouth", "music", "night",
    "noise", "north", "novel", "nurse", "ocean", "offer", "order", "other", "owner", "panel",
    "paper", "party", "peace", "phase", "phone", "photo", "piece", "pilot", "pitch", "place",
    "plane", "plant", "plate", "point", "power", "press", "price", "pride", "prize", "proof",
    "queen", "radio", "range", "ratio", "reach", "reply", "right", "river", "round", "route",
    "scale", "scene", "scope", "score", "sense", "shape", "share", "sheet", "shift", "world"
]

words = []
celebration = ""
announcement = ""
at = ""
mistake = ""
start = ""
fail = ""
ask = ""
end = ""
lang = 0
flag = False

# EN - Initializing variables RU - инициализируем переменные

print("Select game language / Выберите язык игры (1-RU, 2-EN): ")

while lang != 1 and lang != 2:
    lang = input()
    if not lang.isdigit() or int(lang) not in (1, 2):
        print("Write 1 or 2! / Напишите 1 или 2!")
        lang = 0
        continue
    lang = int(lang)
    if lang == 1:
        start = "Попробуйте угадать слово из 5 букв!"
        words = wordsRU
        celebration = "Поздравляю вы отгадали слово!"
        announcement = "Загаданное слово было:"
        at = "Текущая попытка:"
        mistake = "Вы опечатались!"
        fail = "Вы проиграли! В следующий раз получиться!"
        ask = "Хотите-ли сыграть еще раз? (y/n) "
        end = "Нажмите любую клавишу..."
    elif lang == 2:
        words = wordsEN
        start = "Try to guess a 5-letter word!"
        celebration = "My Congratulations!"
        announcement = "Hidden word was:"
        at = "Current attempt: "
        mistake = "You made a typo!"
        fail = "You lost! Better luck next time!"
        ask = "Would you like to play again? (y/n)"
        end = "Press any key..."
    # EN - asking and apply language  RU - спрашиваем и применяем язык

# контейнер из 120 сгенерированных рандомных слов

while True:

    print(start)
    goal = words[random.randint(0, len(words) - 1)] # EN - generate random word as a secret word from the list RU - генерируем загаданное слово из списка
    t = ""
    attempt = 0
    while attempt != 6:
        print(at, attempt)
        a = input()
        attempt += 1
        if len(a) != 5:
            print(mistake)
            attempt -= 1
            continue
        for check in range(5):
            if a[check].lower() == goal[check]:
                t += "🟩"
            elif a[check].lower() in goal:
                t += "🟨"
            else:
                t += "🟥"
        print(t)
        if t == "🟩🟩🟩🟩🟩":
            flag = True
            break

        t = ""

    # EN - game script RU - непосредственно код игры

    if flag is True:      # EN - win RU - Выигрыш
        print(celebration)
        print(announcement, goal)
        flag = False
    else:     # EN - fail RU - Проигрыш
        print(fail)
        print(announcement, goal)

    ans = input(ask)
    if ans.lower() == "y":
        print()
    else:
        break

input(end)
exit(0)
