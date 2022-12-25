#1 задание - Взять 2 списка, 1(Марка автомобилей) 2( цены), сделать словарь из двух списков.
a=("Audi", "Acura", "BMW", "CHEVROLET", "FERRARI")
b=(5000, 9000, 12000, 15000, 18000)
c=dict(zip(a,b))
print(c)

#2 задание - Из словаря сделать запись в CSV таблицу, с помощью модуля CSV, 1 значение одна колонка, для 2-го другая колонка.
def createCSV(path, dict):
    writer=csv.writer(open(path, 'w' , newline=''))
    for i in range(len(dict)):
        keys=list(dict.keys())
        values=list(dict.values())
        writer.writerow(keys[i], values[i])
#3 задание - Взять произвольный текст, сохранить в формате txt Блокнот, прочитать его с помощью питона и найти количество букв "о"(любые буквы) в тексте.
with open('Randomtext.txt', 'r') as file:
    content = file.read()
    a = content.count('t')
    print(a)