#coding:utf-8
import requests
import json
from article import Article
from author import Author

def str_to_object_list(string, class_object):
    list_json = json.loads(string)
    lists = []
    for dictionary in list_json:
        lists.append(class_object(dictionary))
    return lists

def article_match_author(filename):
    with open(filename, "w") as file:
        for article in articles:
            for author in authors:
                if article.is_written_by(author):
                    file.writelines("标题:{},作者{}\n".format(article.title, author.name))
                else:
                    continue

if __name__ == "__main__":
    print "==>begin"

    respon_article = requests.get("http://jsonplaceholder.typicode.com/posts")
    articles =  str_to_object_list(respon_article.content,Article)

    respon_author = requests.get("http://jsonplaceholder.typicode.com/users")
    authors = str_to_object_list(respon_author.content,Author)
    article_match_author("file.txt")

    print "==>over"

