class Configuration(object):

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1111@localhost/table1'
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECRET_KEY = "something very secret"
    PAGES_DIR = 'pages'
    EMAIL_ADDRESS = "workakkount99@gmail.com"
    PASSWORD = "rybasher2281899"
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = "sha512_crypt"

