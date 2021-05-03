import random
import time

def display_intro():
    print("********************\nСйечас сыграем в игру камень, ножницы бумага")

def choose_vybor():
    vybor=input("Выбери Цифру:\n1.Камень\n2.Ножницы\n3.Бумага: ")
    while vybor!="1" and vybor!="2" and vybor!="3":
        choose_vybor()
    return int(vybor)

def check_vybor(chosenvybor):
    rightvybor = random.randint(1,3)
    if chosenvybor==rightvybor:
        print("Ничья")
    elif chosenvybor==1 and rightvybor == 2:
        print("Вы выйграли")
    elif chosenvybor==1 and rightvybor == 3:
        print("Вы проиграли")
    elif chosenvybor==2 and rightvybor == 1:
        print("Вы проиграли")
    elif chosenvybor==2 and rightvybor == 3:
        print("Вы выйграли")
    elif chosenvybor==3 and rightvybor == 1:
        print("Вы выйграли")
    elif chosenvybor==3 and rightvybor == 2:
        print("Вы проиграли")

        ###########################

option = "yes"
while option == "yes":
    option=input("Сыграем? (yes/no) - ")
    if option == "yes":
        display_intro()
        time.sleep(2)
        check_vybor(choose_vybor())
        time.sleep(2)