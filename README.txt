Banking Transactions API

This is a simple banking transactions API built using Flask and Flask-Injector. The API handles user accounts and transactions between these accounts.
Requirements

    Python 3.6+
    Flask
    Flask-Injector
    Pydantic

Installation

    Clone the repository:

    sh

git clone <repository-url>
cd <repository-directory>

Create and activate a virtual environment:

sh

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

Install dependencies:

sh

    pip install Flask Flask-Injector pydantic

Running the Application

    Run the Flask application:

    sh

    python app.py

    The application will be running at http://127.0.0.1:5000/.

API Endpoints

    Create a New User Account with an Initial Balance

    Endpoint: POST /api/account

    Request Body:

    json

{
    "account_id": 1,
    "initial_balance": 100.0
}

Example using curl:

sh

curl -X POST http://127.0.0.1:5000/api/account \
-H "Content-Type: application/json" \
-d '{"account_id": 1, "initial_balance": 100.0}'

Example using Postman:

    Create a new POST request to http://127.0.0.1:5000/api/account.
    Set the request body to JSON:

json

{
    "account_id": 1,
    "initial_balance": 100.0
}

    Send the request.

Transfer Funds from One Account to Another

Endpoint: POST /api/transfer

Request Body:

json

{
    "from_account_id": 1,
    "to_account_id": 2,
    "amount": 50.0
}

Example using curl:

sh

curl -X POST http://127.0.0.1:5000/api/transfer \
-H "Content-Type: application/json" \
-d '{"from_account_id": 1, "to_account_id": 2, "amount": 50.0}'

Example using Postman:

    Create a new POST request to http://127.0.0.1:5000/api/transfer.
    Set the request body to JSON:

json

{
    "from_account_id": 1,
    "to_account_id": 2,
    "amount": 50.0
}

    Send the request.

Retrieve the Transaction History for a Given Account

Endpoint: GET /api/transactions/<account_id>

Example using curl:

sh

    curl -X GET http://127.0.0.1:5000/api/transactions/1

    Example using Postman:
        Create a new GET request to http://127.0.0.1:5000/api/transactions/1.
        Send the request.

Example Workflow

    Create Accounts:

    sh

curl -X POST http://127.0.0.1:5000/api/account \
-H "Content-Type: application/json" \
-d '{"account_id": 1, "initial_balance": 100.0}'

curl -X POST http://127.0.0.1:5000/api/account \
-H "Content-Type: application/json" \
-d '{"account_id": 2, "initial_balance": 200.0}'

Transfer Funds:

sh

curl -X POST http://127.0.0.1:5000/api/transfer \
-H "Content-Type: application/json" \
-d '{"from_account_id": 1, "to_account_id": 2, "amount": 50.0}'

Retrieve Transaction History:

sh

    curl -X GET http://127.0.0.1:5000/api/transactions/1

Conclusion

This simple banking transactions API allows you to create user accounts, transfer funds between accounts, and retrieve transaction history. Feel free to extend and enhance the functionality as needed.
