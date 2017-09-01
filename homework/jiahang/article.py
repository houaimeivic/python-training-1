class Article(object):
    def __init__(self, dictionary):
        self.user_id = dictionary["userId"]
        self.id = dictionary["id"]
        self.title = dictionary["title"]
        self.body = dictionary["body"]
    def is_written_by(self,author):
        return self.user_id == author.id

    def __str__(self):
        return ("Article:{{user_id : {},id : {},title : {},body : {}}}"
                .format(self.user_id,self.id,self.title,self.body))
    __repr__ = __str__
