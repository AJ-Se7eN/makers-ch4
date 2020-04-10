"""def percent(a):
    upper=0 #переменная, которая будет принимать заглавные
    lower=0 #переменная, которая будет принимать строчные
#убираю спец символы, а так же пробел
    symbols=["!" , "," , "@" , "." , "?" , ":" , ";" , "/","`"," "]
    for symbol in symbols:
        if symbol in text:
            new_text=text.replace(symbol,"")
    lens=len(new_text)
#функция в диапозоне lens
#буквы по одной проверяются на пропись
    for i in range (lens):
        a=new_text[i]
        if a.isupper():
            upper+=1
        elif a.islower():
            lower += 1
#высчитывает проценты из условия что new_text(то есть текст без спец символов) = 100%
    upper1=(upper*100)/lens
    lower1=(lower*100)/lens
    print("заглавных -",str(round(upper1)) + '%')
    print("строчных -",str(round(lower1)) + '%')
text=input("Введите ваш текст: ")
percent(text)

"""
    
