from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from dtos.account_dto import CreateAccountDTO, TransferFundsDTO
from services.account_service import AccountService

account_bp = Blueprint('account', __name__)

def init_account_controller(account_service: AccountService):
    @account_bp.route('/account', methods=['POST'])
    def create_account():
        try:
            account_data = CreateAccountDTO(**request.json)
            account_service.create_account(account_data)
            return jsonify({"message": "Account created successfully"}), 201
        except ValidationError as e:
            return jsonify(e.errors()), 400

    @account_bp.route('/transfer', methods=['POST'])
    def transfer_funds():
        try:
            transfer_data = TransferFundsDTO(**request.json)
            account_service.transfer_funds(transfer_data)
            return jsonify({"message": "Transfer successful"}), 200
        except ValidationError as e:
            return jsonify(e.errors()), 400
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @account_bp.route('/transactions/<int:account_id>', methods=['GET'])
    def get_transactions(account_id):
        transactions = account_service.get_transactions(account_id)
        if transactions is None:
            return jsonify({"error": "Account not found"}), 404
        return jsonify({"transactions": transactions}), 200

    return account_bp

