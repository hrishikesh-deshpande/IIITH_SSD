
import requests
from flask import request, Flask

username = ""


def try_register():
    print('register')
    username = input('Enter Username : ')
    password = input('Enter Password : ')
    json = {'username': username, 'password': password}
    response = requests.post(
        'http://localhost:50551/user/register', json=json).content.decode()
    print(response)


def try_login():
    print('login')
    username = input('Enter Username : ')
    password = input('Enter Password : ')
    json = {'username': username, 'password': password}
    response = requests.post(
        'http://localhost:50551/user/login', json=json).content.decode()
    print(response)


def try_logout():
    print('logout')
    global username
    json = {'username': username}
    response = requests.post(
        'http://localhost:50551/user/logout', json=json).content.decode()
    print(response)
    username = ""


if __name__ == "__main__":
    try_register()
    try_login()
    try_logout()
