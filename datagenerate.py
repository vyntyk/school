import random

#import csv
#import logger as lg

file = open('base_phone.csv', 'w')
newrecord = "ID,Name,Surname,BirthDay,PhoneNumber,Classes,Salary\n"

import csv
import logger as lg

file = open('base_phone.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber,email\n"
file.writelines(newrecord)

ls_name = ['Lana', 'Dima', 'Anna', 'Natasha', 'Pasha', 'Denis', 'Kate', 'Sonya', 'Roma', 'Igor', 'Lina']
ls_surname = ['Petrenko', 'Ivanov', 'Nebozenko', 'Kaleeva', 'Zinchenko', 'Kushnir', 'Krasota', 'Usenko', 'Morozov',
              'Fomenko', 'Vitek']

ls_birthday = ['20.05.1984', '30.01.1993', '14.03.1976', '12.02.1987', '24.07.1967', '29.03.1990', '24.06.1990', 
                '19.02.1985', '14.03.1997', '27.05.1997', '13.05.1987']
ls_classes = ['mathematics', 'informatics', 'english language', 'physical culture', 'history',
             'social studies', 'philosophy', 'geography', 'literature']

ls_e_mail = ['11111@gmail.com', '2222222@yandex.ru', '333333@mail.ru', '44444444@gmail.com', '5555555@gmail.com',
             '666666666@mail.ru', '77777777@mail.ru', '88888888@mail.ru', '99999999@yandex.ru']



def list_of_numbers():
    randomListPhone = random.randint(79000000000, 80000000000)
    return str(randomListPhone)

def list_of_salary():
    randomListSalary = random.randint(10000, 50000)
    return str(randomListSalary)


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + random.choice(ls_birthday) + ',' + list_of_numbers() + ',' + random.choice(ls_classes) + ',' + list_of_salary()


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + list_of_numbers() + ',' + random.choice(
        ls_e_mail)

    return s


def start():
    for i in range(50):
        a = f'{str(i + 1)},{string_creation()} \n'
        file.write(a)
    file.close()


start()
