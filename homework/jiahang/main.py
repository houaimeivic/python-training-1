#coding:utf-8
import requests
import json
from article import Article
from author import Author

def str_to_object_list(str,object):
    list_json = json.loads(str)
    lists = []
    for dict in list_json:
        lists.append(object(dict))
    return lists

def article_match_author(filename):
    clear_file = open(filename, "w")
    clear_file.close()
    file = open(filename, "a")
    try:
        for article in articles:
            for author in authors:
                if article.is_written_by(author):
                    file.writelines("标题:{},作者{}\n".format(article.title, author.name))
    except Exception as e:
        print e.message
    finally:
        file.close()

if __name__ == "__main__":
    print "==>begin"

    respon_article = requests.get("http://jsonplaceholder.typicode.com/posts")
    articles =  str_to_object_list(respon_article.content,Article)

    respon_author = requests.get("http://jsonplaceholder.typicode.com/users")
    authors = str_to_object_list(respon_author.content,Author)
    article_match_author("file.txt")

    print "==>over"

