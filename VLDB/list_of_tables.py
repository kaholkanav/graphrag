import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('banking_system.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the query to list all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()

sql_files = [
    'Clearing_houses.sql', 'direct_debits.sql', 'Recurring_Payments.sql', 'employee_details.sql',
    'Settlement_Partners.sql', 'fixed_deposit_accounts.sql', 'Settlement_Reconciliation.sql', 'forex_transactions.sql',
    'Standing_orders.sql', 'fraud_alerts.sql', 'account_balances.sql', 'international_payments.sql',
    'account_holder.sql', 'investment_accounts.sql', 'account_master.sql', 'loan_accounts.sql',
    'account_statement.sql', 'loan_applications.sql', 'anti_money_laundering_reports.sql', 'loan_collateral_details.sql',
    'audit_logs.sql', 'loan_defaults.sql', 'bank_charges.sql', 'loan_interest_details.sql',
    'branch_details.sql', 'loan_repayment_schedules.sql', 'cheque_clearing.sql', 'mortgage_accounts.sql',
    'commercial_lending.sql', 'overdraft_accounts.sql', 'compliance_logs.sql', 'payment_instructions.sql',
    'contact_details.sql', 'regulatory_reports.sql', 'corporate_accounts.sql', 'risk_exposure.sql',
    'credit_score_reports.sql', 'savings_account.sql', 'creditcard_accounts.sql', 'settlement_data.sql',
    'customer_complaints.sql', 'settlement_disputes.sql', 'customer_kyc_details.sql', 'transaction_charges.sql',
    'customer_master.sql', 'transaction_fees.sql', 'customer_risk.sql', 'transaction_master.sql',
    'customer_transaction_history.sql'
] 

#compare the tables in the database with the sql files
for table in tables:
    if table[0] in sql_files:
        sql_files.remove(table[0])
    else:
        print(f"{table[0]} is not in the sql files")

# Print the list of tables
# for table in tables:
#     print(table[0])

# Close the connection
conn.close()