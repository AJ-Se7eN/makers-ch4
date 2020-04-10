# kolich=int(input())
# a=0 #отвечает за начало функции
# b=1 #отвечает за шаг
# c=2 #временная переменная
# x=[]
# while len(x)<kolich:
#     c=a+b
#     a=b
#     b=c
#     x.append(a)
# print(x)





kolich=int(input("Сколько чисел вывести?:"))
start=0
step=int(input("Укажите шаг функции:"))
list_=[]
while len(list_)<kolich:
    c=start+step
    start=step
    step=c
    list_.append(start)
print(list_)