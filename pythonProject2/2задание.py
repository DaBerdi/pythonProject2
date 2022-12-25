#2 задание - Из словаря сделать запись в CSV таблицу, с помощью модуля CSV, 1 значение одна колонка, для 2-го другая колонка.



def createCSV(path, dict):
    writer= csv.writer(open(path, 'w' , newline=''))
    for i in range(len(dict)):
        keys=list(dict.keys())
        values=list(dict.values())
        writer.writerow([keys[i], values[i]])