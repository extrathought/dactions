__author__ = 'wolf'

class User:
    """The site users and members"""

    name = None
    mail = None
    twitter = None

    def __init__(self, name, mail, twitter):
        self.name = name
        self.mail = mail
        self.twitter = twitter