import json
command = 0
users = {}
with open('databased.json', 'r') as j:
    text = j.read()
    list_of_users = json.loads(text)
def displayMenu():
        status = input("Вы уже были зарегистрированы?")
        if status == "Да":
            oldUser()
        elif status == "Нет":
            newUser()
def newUser():
    createLogin = input("Введите логин: ")
    if createLogin in list_of_users or createLogin in users:
        print("Логин уже используется")
    else:
        createPassw = input("Введите пароль: ")
        list_of_users[createLogin] = createPassw
        print("Регистрация прошла успешно!")
        with open('databased.json', 'w') as j:
            text = json.dumps(list_of_users)
            j.write(text)


def oldUser():
    login = input("Введите ваш логин: ")
    passw = input("Введите ваш пароль: ")
    if login in list_of_users and list_of_users[login] == passw:
        print("Вход выполнен")
        global command
        command = 1
    else:
        print("Введён неверный логин или пароль")

while command != 1:
    displayMenu()

