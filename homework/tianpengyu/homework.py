import requests
import json


users = []
user = {}

def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return json.loads(response.content)

def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return json.loads(response.content)

def find_by_id(id,title,get_user):
    for msg in get_user:
        if(msg['id']==id):
            user['title'] = title
            user['name'] = msg['name']
            users.append(user)


def main():
    global users
    posts = get_posts()
    get_user = get_users()
    for user in posts:
        find_by_id(user['id'],user['title'],get_user)
    file = open('data.txt','w')
    file.writelines(['{}\n'.format(line) for line in users])


if __name__ == '__main__':
    main()