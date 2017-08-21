class Author(object):
    def __init__(self,dict):
        self.id = dict["id"]
        self.name = dict["name"]
        self.username = dict["username"]
        self.email = dict["email"]
        self.address = dict["address"]
        self.phone = dict["phone"]
        self.website = dict["website"]
        self.company = dict["company"]
