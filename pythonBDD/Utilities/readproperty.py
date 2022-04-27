import configparser
config = configparser.RawConfigParser()
config.read(".\\pythonBDD\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common-info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common-info', 'userName')
        return username

    @staticmethod
    def getFirstName():
        firstname = config.get('common-info', 'firstName')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('common-info', 'lastName')
        return lastname

    @staticmethod
    def getEmail():
        email = config.get('common-info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common-info', 'passWord')
        return password

    @staticmethod
    def getConPassword():
        conpassword = config.get('common-info', 'conpassWord')
        return conpassword

