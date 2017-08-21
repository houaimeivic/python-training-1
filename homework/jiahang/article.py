class Article(object):
    def __init__(self,dict):
        self.user_id = dict["userId"]
        self.id = dict["id"]
        self.title = dict["title"]
        self.body = dict["body"]
    def is_written_by(self,author):
        return self.user_id == author.id

    def __str__(self):
        return ("Article:{{user_id : {},id : {},title : {},body : {}}}"
                .format(self.user_id,self.id,self.title,self.body))
    __repr__ = __str__