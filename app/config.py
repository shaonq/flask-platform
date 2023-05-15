import os

DEBUG = False
TESTING = False
VUE_INDEX = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dist/index.html')
SECRET_KEY = '9GxNuF-dI%T*(#jr'
UPLOAD_FILE_PATH =  os.path.join(os.path.dirname(__file__), 'upload_file')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:123456@127.0.0.1/mysql_db')
SQLALCHEMY_TRACK_MODIFICATIONS = False    # 请求结束自动提交数据库


# production
if os.environ.get("APP_ENV") == "production":
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:123456@py-mysql/mysql_db')
    DEBUG = False
