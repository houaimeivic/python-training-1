#encoding=utf-8
import requests
import json
import os


#  获取数据 #
name = []
author = []
class  get_data():
    def  get_author_data(url_author):
        html = requests.get(url_author)
        get_html_data = html.json()
        for item in get_html_data:
            object_data_author = {
                'userId': item["userId"],
                'title': item["title"]
            }
            author.append(object_data_author)
            #print author
    get_author_data('https://jsonplaceholder.typicode.com/posts')

    def get_name_data(url_name):
        html_name = requests.get(url_name)
        get_html_name_data = html_name.json()
        # print get_html_name_data
        for item_name in get_html_name_data:
            object_data_name = {
                'id ': item_name['id'],
                'name': item_name['name']
            }
            name.append(object_data_name)
    get_name_data('http://jsonplaceholder.typicode.com/users')

#  清洗数据  #
result = []
def result_data():
    for item_author in author:
        for item in name:
            if item['id '] == item_author['userId']:
                object_result = {
                    'title': item_author['title'],
                    'author': item['name']
                }
                result.append(object_result)
 #   print result

result_data()
# 写文件 #
def writing_file():
    write_file = open('file_content1.txt', 'w')
    for content in result:
        write_file.writelines('标题：{}，作者：{}\n'.format(content['title'], content['author']))
    write_file.close()
writing_file()



