from django.urls import path
from .views import customer_profile, edit_loan, edit_wallet, list_customers, list_wallets, register_account, register_card, register_customer, register_loan, register_receipt, register_third_party, register_wallet, register_transaction, register_notification, register_reward, register_currency, edit_customer, wallet_profile, list_accounts, account_profile, edit_account, list_transactions, transaction_profile, edit_transaction, list_cards, card_profile, edit_card, list_third_partys, third_party_profile, edit_third_party, list_notifications, notification_profile, edit_notification, list_receipts, receipt_profile, edit_receipt, list_loans, loan_profile, list_rewards, reward_profile, edit_reward, list_currencys, currency_profile, edit_currency


urlpatterns = [
    path("register/", register_customer, name ="registration"),  
    path("list/", list_customers, name ="list_customers"),
    path("customers/<int:id>", customer_profile, name ="customer_profile"),
    path("customers/edit/<int:id>", edit_customer, name ="edit_customer"),
]