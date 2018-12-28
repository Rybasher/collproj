import xml.etree.ElementTree as ET


tree = ET.parse('cars1.xml')
root = tree.getroot()


def  find_user(l, u):
    for i in root.findall('car'):
        if i.findtext(l) == ch:
            name = i.find('mark')
            print(name.text)


for car in root.findall('car'):

    for char in car.findall('mark'):
        print(char.tag,":", char.text)

    for char in car.findall('Year'):
        print(' - ', char.tag,':',char.text)

    for char in car.findall('Model'):
        print(' - ', char.tag,':',char.text)

    for char in car.findall('distance'):
        print(' - ', char.tag,':', char.text)

    for char in car.findall('Type'):
        print(' - ', char.tag,':',char.text)

    for char in car.findall('Vechicle'):
        print(' - ', char.tag,':',char.text)

    for char in car.findall('Owner'):
        print(' - ', char.tag,':',char.text)


run = 1
while run == 1:

    choice = input("Введите критерий поиска(1.Пользователь/2.Пробег/3.Вместе): ")

    if choice == "1":
        l = 'Owner'
        ch = input("Введите имя пользователя: ")
        find_user(l,ch)

    elif choice == "2":
        l = 'distance'
        ch = input("Введите пробег: ")
        find_user(l,ch)

    elif choice == "3":
        l = "Owner"
        l1 = "distance"
        ch = input("Введите пользователя: ")
        ch1 = input("Введите пробег: ")
        for actor in root.findall('car'):
            if (actor.findtext(l) == ch) and (actor.findtext(l1) == ch1):
                name = actor.find('mark')
                print(name.text)

    else:
        print("Вы ввели значение не входящее в диапазон. Попробуйте еще раз.")
        continue

