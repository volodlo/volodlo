import json
command = None
users = {}
list_of_users = {}
def displayMenu():
        status = input("Вы уже были зарегистрированы?")
        if status == "Да":
            oldUser()
        elif status == "Нет":
            newUser()
def newUser():
    with open('databased.json', 'r') as j:
        text = j.read()
        list_of_users = json.loads(text)
    createLogin = input("Введите логин: ")

    if createLogin in list_of_users:
        print("Логин уже используется")
    else:
        createPassw = input("Введите пароль: ")
        users[createLogin] = createPassw
        print("Регистрация прошла успешно!")
        list_of_users.append(users)
        with open('databased.json', 'w') as j:
            text = json.dumps(list_of_users)
            j.write(text)


def checkKey(dic, key):
    if key in dic:
        print("Present, ", end=" ")
        print("value =", dic[key])
    else:
        print("Not present")


def oldUser():
    login = input("Введите ваш логин: ")
    passw = input("Введите ваш пароль: ")
    if login in users and users[login] == passw:
        print("Вход выполнен")
    else:
        print("Введён неверный логин или пароль")

while True:
    displayMenu()

