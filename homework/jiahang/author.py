class Author(object):
    def __init__(self, dictionary):
        self.id = dictionary["id"]
        self.name = dictionary["name"]
        self.username = dictionary["username"]
        self.email = dictionary["email"]
        self.address = dictionary["address"]
        self.phone = dictionary["phone"]
        self.website = dictionary["website"]
        self.company = dictionary["company"]
