t=True
while t:
    print("выберите помощь которая вам нужна:Погода, Дата, Шутка либо введите 0 чтобы закрыть программу")
    zapros=input("введите ваш запрос: ")
    if zapros=="Погода" or zapros=="Дата" or zapros=="Шутка" or zapros=="0":
        print("Ваш запрос выполнен")
        if zapros=="Погода":
            print("Погода в Минске или в Москве?")
            pogoda=input("Выберите город: ")
            if pogoda=="Минск":
                print("На сегодня или на завтра")
                den=input("Выберите день: ")
                if den=='сегодня':
                    print("-2,Cнег")
                elif den=="завтра":
                    print("+2,Солнечно")
            elif pogoda=="Москва":
                print("На сегодня или на завтра")
                den=input("Выберите день: ")
                if den=='сегодня':
                    print("-1,Cнег")
                elif den=="завтра":
                    print("+5,Солнечно")
        elif zapros=="Дата":
            print("28.12.2020")
        elif zapros=="Шутка":
            print("шутка на русском или на английском?")
            yazik=input("Введите выбранный язык: ")
            if yazik=="Русский":
                print("Надежда всегда умирает последней, поэтому никогда не женитесь на Надеждах")
            if yazik=="Английский":
                print("Kolobok goes to the bathhouse, comes out and says: «Damn, forgot to wash my head!")
        elif zapros=="0":
            t=False
    else:
        print("Запрос введен неверно")
