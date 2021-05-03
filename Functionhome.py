#def short_story():
  #print("Перемен требуют наши сердца")
#  print("Перемен, Ьребуют наши глаза")
 # print("В нашем смехе и в наших сердцах и в пульсации вен")
  #print("Перемен.  Мы ждем перемен")
#short_story()
#def short_story():
#	print("У попа была собака, он ее любил.")    
#	print("Она съела кусок мяса, он ее убил,")    
#	print("В землю закопал и надпись написал:")
#	short_story()

############################3
#def chek ():
#    rojok=int(input("Введите количество рожков: "))
#    price = rojok*100
#    print(price)
#    return price
    
#    #################
#print("Выберите вкус желаемого мороженного\n1)Клубничное\n2)Шоколадной\n3)Ванильное")
#vkus=int(input("Введите ваш выбор: "))
#if vkus == 1:
#  print("Вы выбрали клубничное мороженое")
#  print(chek())
#elif vkus == 2:
#    print("Вы выбрали шоколадное мороженое")
#    print(chek())
#elif vkus == 3:
#    print("Вы выбрали ванильное мороженое")
#    print(chek())
#else:
#    print ("Начните свой выбор заново")

#######################
def translate ():
  speed = int(input("Введите значение скорости: "))
  skorost = speed * 1000 / 3600 
  print(skorost, "км/ч")
  #######################

def minmax ():
  znach1 = int(input("Введите первое значение: "))
  znach2 = int(input("Введите второе значение: "))
  znach3 = int(input("Введите трктьк значение: "))
  otvet = min(znach1, znach2, znach3)  
  print(otvet)
  ########################

def stepeni ():
  chislo = int(input("Введите число "))
  stepen = int(input("Введите степень"))
  for stepen in range[1,stepen]:
    otvet = chislo**stepen
    print(otvet)
stepeni ()