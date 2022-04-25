from os import getenv
from flask import Flask

from router import router_blueprint
from switches import switches_blueprint
from configuration import configuration_blueprint

from dotenv import load_dotenv
from db import DB


# create flask instance
app = Flask(__name__)

# mount endpoint defined from other files
app.register_blueprint(router_blueprint, url_prefix='/devices/routers')
app.register_blueprint(switches_blueprint, url_prefix='/devices/switches')
app.register_blueprint(configuration_blueprint, url_prefix='/configure')

@app.route('/test', methods=['GET'])
def test() -> str:
    return 'Test succeded!'

# load environment variables from '.env' file
load_dotenv()

# db connection
dsn = f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@{getenv("DB_HOST")}:{getenv("DB_PORT")}/{getenv("DB_NAME")}?sslmode=disable'
DB.init(dsn)


