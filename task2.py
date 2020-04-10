#сплитуем по пробелам
text=input().split(" ")
#сортируем по длинне с помощью ключа len
text.sort(key=len)
#обратно раставляем пробелы и соединяем
new_text=" ".join(text)
print(new_text)