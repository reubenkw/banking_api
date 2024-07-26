from flask import Flask
from flask_injector import FlaskInjector
from injector import inject, singleton

from controllers.account_controller import init_account_controller
from services.account_service import AccountService
from repositories.account_repository import AccountRepository

def configure(binder):
    binder.bind(AccountRepository, to=AccountRepository, scope=singleton)
    binder.bind(AccountService, to=AccountService, scope=singleton)

def create_app():
    app = Flask(__name__)
    
    # Root endpoint
    @app.route('/')
    def home():
        return "Banking Transactions API is running", 200
    
    account_repository = AccountRepository()
    account_service = AccountService(account_repository)
    account_controller = init_account_controller(account_service)
    app.register_blueprint(account_controller, url_prefix='/api')
    return app

app = create_app()

FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True)

