import random
gamer=0
computer=0
num=int(input("На сколько игроков? 1 or 2: "))

while True:
    g=input("камень,ножницы,бумага?: ").lower()

    if num==1:
        list_=("камень","ножницы","бумага")
        c=random.choice(list_)
        print(c)
    elif num==2:
        c=input("камень,ножницы,бумага?: ").lower()

    if g=="камень" and c=="ножницы":
        gamer+=1
    elif g=="камень" and c=="бумага":
        computer+=1
    elif g=="ножницы" and c=="бумага":
        gamer+=1
    elif g=="ножницы" and c=="камень":
        computer+=1
    elif g=="бумага" and c=="камень":
        gamer+=1
    elif g=="бумага" and c=="ножницы":
        computer+=1
    elif g==c:
        print("ничья")
    else:
        print("уупс!")
    if gamer==3 or computer==3:
        break
    elif g=="выйти" or c=="выйти":
        break
    print(gamer,computer)
if gamer>computer:
    print("Игрок первый выиграл!!!!")
elif gamer<computer and num==2:
    print("Игрок второй выиграл!!!!")
else:
    print("К сожалению компьютер выиграл!!!!")