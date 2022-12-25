#3 задание - Взять произвольный текст, сохранить в формате txt Блокнот, прочитать его с помощью питона и найти количество букв "о"(любые буквы) в тексте.
with open('Randomtext.txt', 'r') as file:
    content = file.read()
    a = content.count('t')
    print(a)