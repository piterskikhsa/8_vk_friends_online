import vk
from getpass import getpass

APP_ID = 6138740


def get_user_login():
    return input('Введите ваш логин: ')


def get_user_password():
    return getpass('Введите ваш пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
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
