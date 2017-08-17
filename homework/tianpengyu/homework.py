# coding=utf-8
import requests
import json

users = []

def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return json.loads(response.content)

def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return json.loads(response.content)

def find_by_id(id,get_user):
    for user in get_user:
        if(user['id']==id):
            return user['name']

def main():
    global users
    posts = get_posts()
    get_user = get_users()
    for user in posts:
        account = {}
        name = find_by_id(user['userId'],get_user)
        account['title'] = user['title']
        account['name'] = name
        users.append(account)
    file = open('data.txt','w')
    file.writelines(['标题:{title},作者:{name}\n'.format(title=line['title'],name=line['name']) for line in users])

if __name__ == '__main__':
    main()