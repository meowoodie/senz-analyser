__author__ = 'woodie'

class SenzException(Exception):

    def __init__(self, type):
        Exception.__init__(self)
        self.type = type
