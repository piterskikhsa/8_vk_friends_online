import vk
from getpass import getpass

APP_ID = 6138740  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input('Введите ваш логин: ')
    return login


def get_user_password():
    password = getpass('Введите ваш пароль: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    # например, api.friends.get()
    friends_online_id = api.friends.getOnline()
    friends_online_name = api.users.get(user_ids=friends_online_id)
    return friends_online_name


def output_friends_to_console(friends_online):
    print('Online: ')
    for friend in friends_online:
        print('{} {} - user_id: {}'.format(friend['last_name'], friend['first_name'], friend['uid']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
