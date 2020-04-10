number= input().split(" ")#принимает и сразу сплитует
foot= int(input())#отвечает за шаг
shifr=[]#путая строка принимающая значения
if foot>0:
    for i in range (len(number)):
        if i+foot<len(number):
            shifr.append(number[i+foot])
        else:
             shifr.append(number[i-foot-1])
elif foot<0:
    for i in range(len(number)):
        shifr.append(number[i+foot])
new_shifr=" ".join(shifr)
print(new_shifr)