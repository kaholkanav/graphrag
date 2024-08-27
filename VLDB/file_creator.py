import os
import uuid
import random
from datetime import datetime, timedelta, date
from sqlalchemy import create_engine, text, select, func
from sqlalchemy.orm import sessionmaker
from faker import Faker

# Initialize Faker
fake = Faker()

# Database connection
engine = create_engine('sqlite:///banking_system.db')  # Replace with your desired database connection
Session = sessionmaker(bind=engine)
session = Session()

# Directory containing SQL files
sql_files_directory = 'sql_files/'  # Replace with the path to your SQL files

# List of all SQL files
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


# Function to execute SQL files and create tables
def execute_sql_files():
    for sql_file in sql_files:
        file_path = os.path.join(sql_files_directory, sql_file)
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        with open(file_path, 'r') as file:
            sql_commands = file.read()
            with engine.connect() as connection:
                try:
                    connection.execute(text(sql_commands))
                    print(f"Executed: {sql_file}")
                except Exception as e:
                    print(f"Failed to execute {sql_file}: {e}")
                    c=input("error detetced on file "+sql_file+" press any key to continue")


# Function to generate and populate data for customer_master table
def populate_customer_master(num_records):
    for _ in range(num_records):
        customer_data = {
            'CustomerName': fake.name(),
            'AccountNumber': fake.bban(),
            'AccountType': random.choice(['Savings', 'Current', 'Fixed Deposit']),
            'Address': fake.address(),
            'ContactNumber': fake.phone_number(),
            'Email': fake.email(),
            'DateOfBirth': fake.date_of_birth(minimum_age=18, maximum_age=75),
            'CustomerSince': fake.date_this_decade(),
            'Status': random.choice(['Active', 'Dormant', 'Closed']),
            'NationalID': fake.ssn(),
            'TaxID': fake.ssn(),
            'EmploymentStatus': random.choice(['Employed', 'Self-Employed', 'Unemployed', 'Retired']),
            'AnnualIncome': round(random.uniform(30000, 150000), 2),
            'RiskProfile': random.choice(['Low', 'Medium', 'High']),
            'MaritalStatus': random.choice(['Single', 'Married', 'Divorced']),
            'NumberOfDependents': random.randint(0, 4),
            'PreferredLanguage': random.choice(['English', 'Spanish', 'French']),
            'PreferredCommunicationChannel': random.choice(['Email', 'Phone', 'SMS']),
        }

        # SQL insert statement
        insert_statement = text("""
            INSERT INTO customer_master (CustomerName, AccountNumber, AccountType, Address, ContactNumber, Email, DateOfBirth,
                                         CustomerSince, Status, NationalID, TaxID, EmploymentStatus, AnnualIncome, RiskProfile,
                                         MaritalStatus, NumberOfDependents, PreferredLanguage, PreferredCommunicationChannel)
            VALUES (:CustomerName, :AccountNumber, :AccountType, :Address, :ContactNumber, :Email, :DateOfBirth, :CustomerSince,
                    :Status, :NationalID, :TaxID, :EmploymentStatus, :AnnualIncome, :RiskProfile, :MaritalStatus, :NumberOfDependents,
                    :PreferredLanguage, :PreferredCommunicationChannel)
        """)

        session.execute(insert_statement, customer_data)

# Function to generate and populate data for other tables (repeat as needed)
def populate_settlement_data(num_records):
    for _ in range(num_records):
        settlement_data = {
            'TransactionID': fake.uuid4(),
            'CustomerID': random.randint(1, num_records),  # Assuming CustomerID corresponds to an existing customer
            'SettlementDate': fake.date_this_decade(),
            'CurrencyCode': random.choice(['USD', 'EUR', 'GBP']),
            'SettlementAmount': round(random.uniform(5000, 100000), 2),
            'FeeAmount': round(random.uniform(10, 100), 2),
            'NetAmount': round(random.uniform(4900, 99500), 2),
            'Status': random.choice(['Completed', 'Pending', 'Failed']),
            'PaymentMethod': random.choice(['Wire Transfer', 'Credit Card', 'ACH']),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'InitiatingParty': fake.name(),
            'InitiatingPartyAccountNumber': fake.bban(),
            'InitiatingBankName': fake.company(),
            'InitiatingBankSWIFT': fake.swift(),
            'ReferenceNumber': fake.bban(),
            'SettlementType': random.choice(['Standard', 'Priority']),
            'FXRate': round(random.uniform(0.8, 1.5), 4),
            'SettlementInstructions': fake.sentence(),
            'CountryCode': random.choice(['US', 'GB', 'FR']),
            'BankCharges': round(random.uniform(5, 50), 2),
            'AdditionalInfo': fake.text(),
        }

        insert_statement = text("""
            INSERT INTO settlement_data (TransactionID, CustomerID, SettlementDate, CurrencyCode, SettlementAmount, FeeAmount, NetAmount,
                                         Status, PaymentMethod, BeneficiaryName, BeneficiaryAccountNumber, BeneficiaryBankName, 
                                         BeneficiaryBankSWIFT, InitiatingParty, InitiatingPartyAccountNumber, InitiatingBankName,
                                         InitiatingBankSWIFT, ReferenceNumber, SettlementType, FXRate, SettlementInstructions,
                                         CountryCode, BankCharges, AdditionalInfo)
            VALUES (:TransactionID, :CustomerID, :SettlementDate, :CurrencyCode, :SettlementAmount, :FeeAmount, :NetAmount,
                    :Status, :PaymentMethod, :BeneficiaryName, :BeneficiaryAccountNumber, :BeneficiaryBankName,
                    :BeneficiaryBankSWIFT, :InitiatingParty, :InitiatingPartyAccountNumber, :InitiatingBankName,
                    :InitiatingBankSWIFT, :ReferenceNumber, :SettlementType, :FXRate, :SettlementInstructions,
                    :CountryCode, :BankCharges, :AdditionalInfo)
        """)

        session.execute(insert_statement, settlement_data)

# Add similar functions for other tables like loan_accounts, transaction_master, etc.

def populate_clearing_houses(num_records):
    for _ in range(num_records):
        clearing_house_data = {
            'ClearingHouseName': fake.company(),
            'ClearingHouseCode': fake.bban(),
            'ContactPerson': fake.name(),
            'ContactNumber': fake.phone_number(),
            'ContactEmail': fake.email(),
            'ClearingHouseSWIFTCode': fake.swift(),
            'ClearingHouseAddress': fake.address(),
            'OperatingHours': f"{random.randint(8, 10)} AM - {random.randint(5, 7)} PM",
            'SettlementFrequency': random.choice(['Hourly', 'Daily']),
            'ComplianceCheckStatus': random.choice(['Passed', 'Failed']),
            'AMLCheckStatus': random.choice(['Passed', 'Failed']),
            'RiskAssessmentScore': random.randint(1, 100),
            'RegulatoryApprovalStatus': random.choice(['Approved', 'Pending']),
            'SettlementInstructions': fake.sentence(),
            'OperationalNotes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO clearing_houses (ClearingHouseName, ClearingHouseCode, ContactPerson, ContactNumber, ContactEmail, 
                                         ClearingHouseSWIFTCode, ClearingHouseAddress, OperatingHours, SettlementFrequency,
                                         ComplianceCheckStatus, AMLCheckStatus, RiskAssessmentScore, RegulatoryApprovalStatus, 
                                         SettlementInstructions, OperationalNotes)
            VALUES (:ClearingHouseName, :ClearingHouseCode, :ContactPerson, :ContactNumber, :ContactEmail, 
                    :ClearingHouseSWIFTCode, :ClearingHouseAddress, :OperatingHours, :SettlementFrequency, 
                    :ComplianceCheckStatus, :AMLCheckStatus, :RiskAssessmentScore, :RegulatoryApprovalStatus, 
                    :SettlementInstructions, :OperationalNotes)
        """)

        session.execute(insert_statement, clearing_house_data)

# Function to populate the `direct_debits` table
def populate_direct_debits(num_records):
    for _ in range(num_records):
        direct_debit_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'DebitAmount': round(random.uniform(50, 1000), 2),
            'DebitDate': fake.date_this_year(),
            'RecurrencePattern': random.choice(['Monthly', 'Quarterly']),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'ReferenceNumber': fake.bban(),
            'AuthorizationCode': fake.bban(),
            'DebitStatus': random.choice(['Active', 'Cancelled']),
            'TransactionID': random.randint(1, num_records),
            'PaymentMethod': random.choice(['Bank Transfer', 'Credit Card']),
            'RiskAssessmentScore': random.randint(1, 100),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO direct_debits (CustomerID, AccountID, DebitAmount, DebitDate, RecurrencePattern, BeneficiaryName, 
                                       BeneficiaryAccountNumber, BeneficiaryBankName, BeneficiaryBankSWIFT, ReferenceNumber, 
                                       AuthorizationCode, DebitStatus, TransactionID, PaymentMethod, RiskAssessmentScore, Notes)
            VALUES (:CustomerID, :AccountID, :DebitAmount, :DebitDate, :RecurrencePattern, :BeneficiaryName, 
                    :BeneficiaryAccountNumber, :BeneficiaryBankName, :BeneficiaryBankSWIFT, :ReferenceNumber, 
                    :AuthorizationCode, :DebitStatus, :TransactionID, :PaymentMethod, :RiskAssessmentScore, :Notes)
        """)

        session.execute(insert_statement, direct_debit_data)

# Function to populate the `recurring_payments` table
def populate_recurring_payments(num_records):
    for _ in range(num_records):
        first_payment_date = fake.date_this_decade().strftime('%Y-%m-%d')
        next_payment_date = fake.date_this_year().strftime('%Y-%m-%d')
        end_date = (datetime.strptime(next_payment_date, '%Y-%m-%d') + timedelta(days=365)).strftime('%Y-%m-%d')
        
        recurring_payment_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'RecurrencePattern': random.choice(['Monthly', 'Weekly']),
            'PaymentAmount': round(random.uniform(100, 1000), 2),
            'PaymentCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'FirstPaymentDate': first_payment_date,
            'NextPaymentDate': next_payment_date,
            'EndDate': end_date,
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'PaymentStatus': random.choice(['Active', 'Inactive']),
            'PaymentMethod': random.choice(['Bank Transfer', 'Direct Debit']),
            'PaymentReference': fake.bban(),
            'RiskAssessmentScore': random.randint(1, 100),
            'Notes': fake.text(),
            'TransactionID': random.randint(1, num_records)
        }

        insert_statement = text("""
            INSERT INTO recurring_payments (CustomerID, AccountID, RecurrencePattern, PaymentAmount, PaymentCurrency, 
                                            FirstPaymentDate, NextPaymentDate, EndDate, BeneficiaryName, BeneficiaryAccountNumber,
                                            BeneficiaryBankName, BeneficiaryBankSWIFT, PaymentStatus, PaymentMethod, PaymentReference,
                                            RiskAssessmentScore, Notes, TransactionID)
            VALUES (:CustomerID, :AccountID, :RecurrencePattern, :PaymentAmount, :PaymentCurrency, :FirstPaymentDate, 
                    :NextPaymentDate, :EndDate, :BeneficiaryName, :BeneficiaryAccountNumber, :BeneficiaryBankName, 
                    :BeneficiaryBankSWIFT, :PaymentStatus, :PaymentMethod, :PaymentReference, :RiskAssessmentScore, 
                    :Notes, :TransactionID)
        """)

        session.execute(insert_statement, recurring_payment_data)

# Function to populate the `employee_details` table
def populate_employee_details(num_records):
    for _ in range(num_records):
        employee_data = {
            'EmployeeName': fake.name(),
            'EmployeeRole': random.choice(['Teller', 'Manager', 'Loan Officer']),
            'BranchID': random.randint(1, num_records),
            'DateOfJoining': fake.date_this_decade(),
            'EmploymentStatus': random.choice(['Active', 'On Leave', 'Resigned']),
            'Salary': round(random.uniform(30000, 150000), 2),
            'ContactNumber': fake.phone_number(),
            'Email': fake.email(),
            'EmployeeAddress': fake.address(),
            'NationalID': fake.ssn(),
            'TaxID': fake.ssn(),
            'PerformanceRating': round(random.uniform(1, 5), 2),
            'LastPromotionDate': fake.date_this_decade(),
            'ReportingManager': fake.name(),
            'Department': random.choice(['Operations', 'Finance', 'HR']),
            'ComplianceTrainingStatus': random.choice(['Completed', 'Pending']),
            'RiskAssessmentScore': random.randint(1, 100),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO employee_details (EmployeeName, EmployeeRole, BranchID, DateOfJoining, EmploymentStatus, Salary, 
                                          ContactNumber, Email, EmployeeAddress, NationalID, TaxID, PerformanceRating, 
                                          LastPromotionDate, ReportingManager, Department, ComplianceTrainingStatus, 
                                          RiskAssessmentScore, Notes)
            VALUES (:EmployeeName, :EmployeeRole, :BranchID, :DateOfJoining, :EmploymentStatus, :Salary, 
                    :ContactNumber, :Email, :EmployeeAddress, :NationalID, :TaxID, :PerformanceRating, 
                    :LastPromotionDate, :ReportingManager, :Department, :ComplianceTrainingStatus, 
                    :RiskAssessmentScore, :Notes)
        """)

        session.execute(insert_statement, employee_data)

# Function to populate the `settlement_partners` table
def populate_settlement_partners(num_records):
    for _ in range(num_records):
        partner_data = {
            'PartnerName': fake.company(),
            'PartnerType': random.choice(['Bank', 'Financial Institution', 'Clearing House']),
            'ContactPerson': fake.name(),
            'ContactNumber': fake.phone_number(),
            'ContactEmail': fake.email(),
            'PartnerSWIFTCode': fake.swift(),
            'PartnerAddress': fake.address(),
            'PartnershipStartDate': fake.date_this_decade(),
            'PartnershipStatus': random.choice(['Active', 'Inactive']),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'AMLCheckStatus': random.choice(['Passed', 'Failed']),
            'RiskAssessmentScore': random.randint(1, 100),
            'SettlementFrequency': random.choice(['Daily', 'Weekly', 'Monthly']),
            'SettlementLimit': round(random.uniform(100000, 1000000), 2),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO settlement_partners (PartnerName, PartnerType, ContactPerson, ContactNumber, ContactEmail, 
                                             PartnerSWIFTCode, PartnerAddress, PartnershipStartDate, PartnershipStatus, 
                                             RegulatoryComplianceStatus, AMLCheckStatus, RiskAssessmentScore, 
                                             SettlementFrequency, SettlementLimit, Notes)
            VALUES (:PartnerName, :PartnerType, :ContactPerson, :ContactNumber, :ContactEmail, 
                    :PartnerSWIFTCode, :PartnerAddress, :PartnershipStartDate, :PartnershipStatus, 
                    :RegulatoryComplianceStatus, :AMLCheckStatus, :RiskAssessmentScore, 
                    :SettlementFrequency, :SettlementLimit, :Notes)
        """)

        session.execute(insert_statement, partner_data)

# Function to populate the `fixed_deposit_accounts` table
def populate_fixed_deposit_accounts(num_records):
    for _ in range(num_records):
        deposit_start_date = fake.date_this_year().strftime('%Y-%m-%d')
        deposit_term_in_months = random.choice([6, 12, 24, 36])
        maturity_date = (datetime.strptime(deposit_start_date, '%Y-%m-%d') + timedelta(days=deposit_term_in_months * 30)).strftime('%Y-%m-%d')
        deposit_end_date = maturity_date
        
        fixed_deposit_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'DepositAmount': round(random.uniform(1000, 100000), 2),
            'InterestRate': round(random.uniform(2.5, 7.5), 2),
            'DepositTermInMonths': deposit_term_in_months,
            'MaturityDate': maturity_date,
            'MaturityAmount': round(random.uniform(1050, 110000), 2),
            'InterestPaymentFrequency': random.choice(['Monthly', 'Quarterly']),
            'PenaltyForEarlyWithdrawal': round(random.uniform(50, 500), 2),
            'WithdrawalRestrictions': random.choice(['Partial Withdrawal Allowed', 'No Early Withdrawal']),
            'AutoRenewal': random.choice([True, False]),
            'NomineeName': fake.name(),
            'NomineeRelation': random.choice(['Spouse', 'Child', 'Parent']),
            'DepositStartDate': deposit_start_date,
            'DepositEndDate': deposit_end_date,
            'DepositStatus': random.choice(['Active', 'Matured', 'Closed']),
            'AccountManagerID': random.randint(1, num_records),
            'TaxWithheld': round(random.uniform(10, 1000), 2),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO fixed_deposit_accounts (CustomerID, AccountNumber, DepositAmount, InterestRate, DepositTermInMonths, 
                                                MaturityDate, MaturityAmount, InterestPaymentFrequency, PenaltyForEarlyWithdrawal, 
                                                WithdrawalRestrictions, AutoRenewal, NomineeName, NomineeRelation, 
                                                DepositStartDate, DepositEndDate, DepositStatus, AccountManagerID, TaxWithheld, 
                                                RegulatoryComplianceStatus, Notes)
            VALUES (:CustomerID, :AccountNumber, :DepositAmount, :InterestRate, :DepositTermInMonths, :MaturityDate, 
                    :MaturityAmount, :InterestPaymentFrequency, :PenaltyForEarlyWithdrawal, :WithdrawalRestrictions, 
                    :AutoRenewal, :NomineeName, :NomineeRelation, :DepositStartDate, :DepositEndDate, :DepositStatus, 
                    :AccountManagerID, :TaxWithheld, :RegulatoryComplianceStatus, :Notes)
        """)

        session.execute(insert_statement, fixed_deposit_data)

# Function to populate the `settlement_reconciliation` table
def populate_settlement_reconciliation(num_records):
    for _ in range(num_records):
        issue_date = fake.date_this_year().strftime('%Y-%m-%d')
        resolution_date = (datetime.strptime(issue_date, '%Y-%m-%d') + timedelta(days=365)).strftime('%Y-%m-%d')
        reconciliation_data = {
            'SettlementID': random.randint(1, num_records),
            'ReconciliationDate': fake.date_this_year(),
            'ReconciliationStatus': random.choice(['Completed', 'Pending', 'Discrepancy']),
            'DiscrepancyAmount': round(random.uniform(100, 10000), 2),
            'DiscrepancyReason': fake.sentence(),
            'AdjustedAmount': round(random.uniform(500, 5000), 2),
            'AdjustmentDetails': fake.sentence(),
            'ClearingHouse': fake.company(),
            'ReconciliationMethod': random.choice(['Automated', 'Manual']),
            'ReconciledBy': fake.name(),
            'ReconciliationTime': fake.time(),
            'ReconciliationNotes': fake.text(),
            'ResolutionDate': resolution_date,
            'ResolutionStatus': random.choice(['Resolved', 'Escalated']),
            'ComplianceCheckStatus': random.choice(['Passed', 'Failed']),
            'AMLCheckStatus': random.choice(['Passed', 'Failed']),
            'FraudCheckStatus': random.choice(['Passed', 'Failed']),
            'AuditStatus': random.choice(['Passed', 'Failed']),
            'RegulatoryApprovalStatus': random.choice(['Approved', 'Pending'])
        }

        insert_statement = text("""
            INSERT INTO settlement_reconciliation (SettlementID, ReconciliationDate, ReconciliationStatus, DiscrepancyAmount, 
                                                   DiscrepancyReason, AdjustedAmount, AdjustmentDetails, ClearingHouse, 
                                                   ReconciliationMethod, ReconciledBy, ReconciliationTime, ReconciliationNotes, 
                                                   ResolutionDate, ResolutionStatus, ComplianceCheckStatus, AMLCheckStatus, 
                                                   FraudCheckStatus, AuditStatus, RegulatoryApprovalStatus)
            VALUES (:SettlementID, :ReconciliationDate, :ReconciliationStatus, :DiscrepancyAmount, :DiscrepancyReason, 
                    :AdjustedAmount, :AdjustmentDetails, :ClearingHouse, :ReconciliationMethod, :ReconciledBy, 
                    :ReconciliationTime, :ReconciliationNotes, :ResolutionDate, :ResolutionStatus, :ComplianceCheckStatus, 
                    :AMLCheckStatus, :FraudCheckStatus, :AuditStatus, :RegulatoryApprovalStatus)
        """)

        session.execute(insert_statement, reconciliation_data)

# Function to populate the `forex_transactions` table
def populate_forex_transactions(num_records):
    for _ in range(num_records):
        transaction_date = fake.date_this_year()
        transaction_date_str = transaction_date.strftime('%Y-%m-%d')
        settlement_date = (datetime.strptime(transaction_date_str, '%Y-%m-%d') + timedelta(days=30)).strftime('%Y-%m-%d')
        
        forex_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'TransactionDate': transaction_date_str,
            'TransactionAmount': round(random.uniform(1000, 100000), 2),
            'BaseCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'TargetCurrency': random.choice(['JPY', 'CAD', 'AUD']),
            'ExchangeRate': round(random.uniform(0.7, 1.5), 4),
            'ConvertedAmount': round(random.uniform(1000, 150000), 2),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'TransactionReferenceNumber': fake.bban(),
            'TransactionStatus': random.choice(['Completed', 'Pending', 'Failed']),
            'SettlementDate': settlement_date,
            'RiskAssessmentScore': random.randint(1, 100),
            'TransactionFees': round(random.uniform(10, 500), 2),
            'RegulatoryCompliance': random.choice(['Passed', 'Failed']),
            'TransactionNotes': fake.text(),
            'TransactionID': random.randint(1, num_records)
        }

        insert_statement = text("""
            INSERT INTO forex_transactions (CustomerID, AccountID, TransactionDate, TransactionAmount, BaseCurrency, 
                                            TargetCurrency, ExchangeRate, ConvertedAmount, BeneficiaryName, 
                                            BeneficiaryAccountNumber, BeneficiaryBankName, BeneficiaryBankSWIFT, 
                                            TransactionReferenceNumber, TransactionStatus, SettlementDate, RiskAssessmentScore, 
                                            TransactionFees, RegulatoryCompliance, TransactionNotes, TransactionID)
            VALUES (:CustomerID, :AccountID, :TransactionDate, :TransactionAmount, :BaseCurrency, :TargetCurrency, 
                    :ExchangeRate, :ConvertedAmount, :BeneficiaryName, :BeneficiaryAccountNumber, :BeneficiaryBankName, 
                    :BeneficiaryBankSWIFT, :TransactionReferenceNumber, :TransactionStatus, :SettlementDate, 
                    :RiskAssessmentScore, :TransactionFees, :RegulatoryCompliance, :TransactionNotes, :TransactionID)
        """)

        session.execute(insert_statement, forex_data)

# Function to populate the `standing_orders` table
def populate_standing_orders(num_records):
    for _ in range(num_records):
        order_start_date = fake.date_this_year()
        order_end_date = (order_start_date + timedelta(days=365)).strftime('%Y-%m-%d')
        standing_order_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'OrderStartDate': fake.date_this_decade(),
            'OrderEndDate': order_end_date,
            'RecurrencePattern': random.choice(['Monthly', 'Weekly']),
            'OrderAmount': round(random.uniform(100, 5000), 2),
            'OrderCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'ReferenceNumber': fake.bban(),
            'OrderStatus': random.choice(['Active', 'Suspended', 'Cancelled']),
            'PaymentMethod': random.choice(['Bank Transfer', 'Direct Debit']),
            'NextOrderDate': fake.date_this_month(),
            'TransactionID': random.randint(1, num_records),
            'RiskAssessmentScore': random.randint(1, 100)
        }

        insert_statement = text("""
            INSERT INTO standing_orders (CustomerID, AccountID, OrderStartDate, OrderEndDate, RecurrencePattern, OrderAmount, 
                                         OrderCurrency, BeneficiaryName, BeneficiaryAccountNumber, BeneficiaryBankName, 
                                         BeneficiaryBankSWIFT, ReferenceNumber, OrderStatus, PaymentMethod, NextOrderDate, 
                                         TransactionID, RiskAssessmentScore)
            VALUES (:CustomerID, :AccountID, :OrderStartDate, :OrderEndDate, :RecurrencePattern, :OrderAmount, 
                    :OrderCurrency, :BeneficiaryName, :BeneficiaryAccountNumber, :BeneficiaryBankName, 
                    :BeneficiaryBankSWIFT, :ReferenceNumber, :OrderStatus, :PaymentMethod, :NextOrderDate, 
                    :TransactionID, :RiskAssessmentScore)
        """)

        session.execute(insert_statement, standing_order_data)

# Function to populate the `fraud_alerts` table
def populate_fraud_alerts(num_records):
    for _ in range(num_records):
        investigation_start_date = fake.date_this_year()
        investigation_end_date = (investigation_start_date + timedelta(days=365)).strftime('%Y-%m-%d')
        fraud_alert_data = {
            'TransactionID': random.randint(1, num_records),
            'CustomerID': random.randint(1, num_records),
            'AlertDate': fake.date_this_year(),
            'AlertType': random.choice(['High Risk', 'Medium Risk']),
            'RiskScore': random.randint(1, 100),
            'AlertStatus': random.choice(['Investigating', 'Resolved', 'Escalated']),
            'TriggeredBy': random.choice(['Rule-Based', 'ML Model']),
            'InvestigationStartDate': fake.date_this_year(),
            'InvestigationEndDate': investigation_end_date,
            'FraudType': random.choice(['Identity Theft', 'Account Takeover']),
            'ResolutionStatus': random.choice(['Resolved', 'Unresolved']),
            'ResolutionDetails': fake.sentence(),
            'InvestigativeFindings': fake.text(),
            'ReportToAuthorities': random.choice([True, False]),
            'Notes': fake.text(),
            'ComplianceCheckStatus': random.choice(['Passed', 'Failed'])
        }

        insert_statement = text("""
            INSERT INTO fraud_alerts (TransactionID, CustomerID, AlertDate, AlertType, RiskScore, AlertStatus, TriggeredBy, 
                                      InvestigationStartDate, InvestigationEndDate, FraudType, ResolutionStatus, ResolutionDetails, 
                                      InvestigativeFindings, ReportToAuthorities, Notes, ComplianceCheckStatus)
            VALUES (:TransactionID, :CustomerID, :AlertDate, :AlertType, :RiskScore, :AlertStatus, :TriggeredBy, 
                    :InvestigationStartDate, :InvestigationEndDate, :FraudType, :ResolutionStatus, :ResolutionDetails, 
                    :InvestigativeFindings, :ReportToAuthorities, :Notes, :ComplianceCheckStatus)
        """)

        session.execute(insert_statement, fraud_alert_data)

# Function to populate the `account_balances` table
def populate_account_balances(num_records):
    for _ in range(num_records):
        account_balance_data = {
            'AccountID': random.randint(1, num_records),
            'BalanceDate': fake.date_this_year(),
            'OpeningBalance': round(random.uniform(1000, 500000), 2),
            'ClosingBalance': round(random.uniform(1000, 500000), 2),
            'AvailableBalance': round(random.uniform(1000, 500000), 2),
            'BlockedAmount': round(random.uniform(0, 5000), 2),
            'OverdraftLimit': round(random.uniform(0, 5000), 2),
            'InterestEarned': round(random.uniform(0, 1000), 2),
            'ChargesIncurred': round(random.uniform(0, 500), 2),
            'BalanceType': random.choice(['Daily', 'Monthly']),
            'CurrencyCode': random.choice(['USD', 'EUR', 'GBP']),
        }

        insert_statement = text("""
            INSERT INTO Account_Balances (AccountID, BalanceDate, OpeningBalance, ClosingBalance, AvailableBalance, 
                                          BlockedAmount, OverdraftLimit, InterestEarned, ChargesIncurred, BalanceType, 
                                          CurrencyCode)
            VALUES (:AccountID, :BalanceDate, :OpeningBalance, :ClosingBalance, :AvailableBalance, 
                    :BlockedAmount, :OverdraftLimit, :InterestEarned, :ChargesIncurred, :BalanceType, 
                    :CurrencyCode)
        """)

        session.execute(insert_statement, account_balance_data)

def populate_international_payments(num_records):
    for _ in range(num_records):
        international_payment_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'PaymentAmount': round(random.uniform(1000, 100000), 2),
            'PaymentDate': fake.date_this_year(),
            'PaymentCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'ExchangeRate': round(random.uniform(0.7, 1.5), 4),
            'ConvertedAmount': round(random.uniform(1000, 150000), 2),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'IntermediaryBankName': fake.company(),
            'IntermediaryBankSWIFT': fake.swift(),
            'PaymentPurpose': fake.sentence(),
            'RegulatoryCompliance': random.choice(['Passed', 'Failed']),
            'AMLCheckStatus': random.choice(['Passed', 'Failed']),
            'TransactionID': random.randint(1, num_records),
            'PaymentStatus': random.choice(['Completed', 'Pending', 'Failed']),
            'ReferenceNumber': fake.bban(),
            'TransactionFees': round(random.uniform(10, 500), 2),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO international_payments (CustomerID, AccountID, PaymentAmount, PaymentDate, PaymentCurrency, 
                                                ExchangeRate, ConvertedAmount, BeneficiaryName, BeneficiaryAccountNumber, 
                                                BeneficiaryBankName, BeneficiaryBankSWIFT, IntermediaryBankName, 
                                                IntermediaryBankSWIFT, PaymentPurpose, RegulatoryCompliance, AMLCheckStatus, 
                                                TransactionID, PaymentStatus, ReferenceNumber, TransactionFees, Notes)
            VALUES (:CustomerID, :AccountID, :PaymentAmount, :PaymentDate, :PaymentCurrency, :ExchangeRate, :ConvertedAmount, 
                    :BeneficiaryName, :BeneficiaryAccountNumber, :BeneficiaryBankName, :BeneficiaryBankSWIFT, 
                    :IntermediaryBankName, :IntermediaryBankSWIFT, :PaymentPurpose, :RegulatoryCompliance, :AMLCheckStatus, 
                    :TransactionID, :PaymentStatus, :ReferenceNumber, :TransactionFees, :Notes)
        """)

        session.execute(insert_statement, international_payment_data)

# Function to populate the `account_holder` table
def populate_account_holder(num_records):
    used_holder_ids = set()

    for _ in range(num_records):
        while True:
            holder_id = random.randint(1000, 9999)
            if holder_id not in used_holder_ids:
                used_holder_ids.add(holder_id)
                break

        account_id = random.randint(1000, 9999)
        customer_id = random.randint(1000, 9999)
        holder_type = random.choice(['Primary', 'Secondary'])
        holder_status = random.choice(['Active', 'Inactive'])
        relationship_with_primary = random.choice(['Parent', 'Sibling', 'Spouse', 'Child'])
        signature_file_path = f'/path/to/signature_{holder_id}.png'
        created_at = datetime.now()
        updated_at = datetime.now()

        insert_statement = text("""
            INSERT INTO account_holders (HolderID, AccountID, CustomerID, HolderType, HolderStatus, 
                                         RelationshipWithPrimary, SignatureFilePath, CreatedAt, UpdatedAt)
            VALUES (:holder_id, :account_id, :customer_id, :holder_type, :holder_status, 
                    :relationship_with_primary, :signature_file_path, :created_at, :updated_at)
        """)

        account_holder_data = {
            'holder_id': holder_id,
            'account_id': account_id,
            'customer_id': customer_id,
            'holder_type': holder_type,
            'holder_status': holder_status,
            'relationship_with_primary': relationship_with_primary,
            'signature_file_path': signature_file_path,
            'created_at': created_at,
            'updated_at': updated_at
        }

        session.execute(insert_statement, account_holder_data)
    session.commit()

# Function to populate the `investment_accounts` table
def populate_investment_accounts(num_records):
    for _ in range(num_records):
        investment_start_date = fake.date_this_decade()
        investment_end_date = investment_start_date + timedelta(days=365)
        
        investment_account_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'InvestmentType': random.choice(['Mutual Fund', 'Stock Portfolio']),
            'InvestmentAmount': round(random.uniform(5000, 500000), 2),
            'RiskProfile': random.choice(['Low', 'Medium', 'High']),
            'PortfolioManager': fake.name(),
            'AccountStatus': random.choice(['Active', 'Closed']),
            'LastValuationDate': fake.date_this_year(),
            'CurrentValue': round(random.uniform(5000, 550000), 2),
            'ReturnOnInvestment': round(random.uniform(2.5, 10.5), 2),
            'InvestmentStartDate': investment_start_date,
            'InvestmentEndDate': investment_end_date,
            'InvestmentTermInMonths': random.choice([12, 24, 36]),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'TaxWithheld': round(random.uniform(100, 10000), 2),
            'AccountManagerID': random.randint(1, num_records),
            'TransactionLimitPerDay': round(random.uniform(500, 50000), 2),
            'DividendPayoutFrequency': random.choice(['Quarterly', 'Annually']),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO investment_accounts (CustomerID, AccountNumber, InvestmentType, InvestmentAmount, RiskProfile, 
                                             PortfolioManager, AccountStatus, LastValuationDate, CurrentValue, 
                                             ReturnOnInvestment, InvestmentStartDate, InvestmentEndDate, 
                                             InvestmentTermInMonths, RegulatoryComplianceStatus, TaxWithheld, 
                                             AccountManagerID, TransactionLimitPerDay, DividendPayoutFrequency, Notes)
            VALUES (:CustomerID, :AccountNumber, :InvestmentType, :InvestmentAmount, :RiskProfile, :PortfolioManager, 
                    :AccountStatus, :LastValuationDate, :CurrentValue, :ReturnOnInvestment, :InvestmentStartDate, 
                    :InvestmentEndDate, :InvestmentTermInMonths, :RegulatoryComplianceStatus, :TaxWithheld, 
                    :AccountManagerID, :TransactionLimitPerDay, :DividendPayoutFrequency, :Notes)
        """)

        session.execute(insert_statement, investment_account_data)
    session.commit()

# Function to populate the `account_master` table
def populate_account_master(num_records):
    used_ids = set()
    
    for _ in range(num_records):
        while True:
            account_id = random.randint(1, num_records * 10)
            if account_id not in used_ids:
                used_ids.add(account_id)
                break
        
        account_master_data = {
            'AccountID': account_id,
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'AccountType': random.choice(['Savings', 'Checking', 'Fixed Deposit']),
            'BranchCode': fake.swift11(),
            'OpeningDate': fake.date_this_decade(),
            'ClosingDate': fake.date_this_decade(),
            'AccountStatus': random.choice(['Active', 'Closed']),
            'CurrentBalance': round(random.uniform(1000, 100000), 2),
            'AvailableBalance': round(random.uniform(1000, 100000), 2),
            'OverdraftLimit': round(random.uniform(0, 5000), 2),
            'InterestRate': round(random.uniform(0.5, 5.0), 2),
            'AccountCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'AccountManagerID': random.randint(1, num_records),
            'IsJointAccount': random.choice([True, False]),
            'NomineeName': fake.name(),
            'NomineeRelation': random.choice(['Spouse', 'Child', 'Parent']),
            'LastTransactionDate': fake.date_this_decade(),
            'AccountTier': random.choice(['Standard', 'Gold', 'Platinum'])
        }

        insert_statement = text("""
            INSERT INTO Account_Master (AccountID, AccountNumber, CustomerID, AccountType, BranchCode, 
                                        OpeningDate, ClosingDate, AccountStatus, CurrentBalance, AvailableBalance, 
                                        OverdraftLimit, InterestRate, AccountCurrency, AccountManagerID, 
                                        IsJointAccount, NomineeName, NomineeRelation, LastTransactionDate, AccountTier)
            VALUES (:AccountID, :AccountNumber, :CustomerID, :AccountType, :BranchCode, 
                    :OpeningDate, :ClosingDate, :AccountStatus, :CurrentBalance, :AvailableBalance, 
                    :OverdraftLimit, :InterestRate, :AccountCurrency, :AccountManagerID, 
                    :IsJointAccount, :NomineeName, :NomineeRelation, :LastTransactionDate, :AccountTier)
        """)

        session.execute(insert_statement, account_master_data)
    session.commit()

# Function to populate the `loan_accounts` table
def populate_account_master(num_records):
    used_ids = set()
    
    for _ in range(num_records):
        while True:
            account_id = random.randint(1, num_records * 10)
            if account_id not in used_ids:
                # Check if account_id already exists in the database
                existing_id = session.execute(text("SELECT AccountID FROM Account_Master WHERE AccountID = :account_id"), {'account_id': account_id}).fetchone()
                if not existing_id:
                    used_ids.add(account_id)
                    break
        
        account_master_data = {
            'AccountID': account_id,
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'AccountType': random.choice(['Savings', 'Checking', 'Fixed Deposit']),
            'BranchCode': fake.swift11(),
            'OpeningDate': fake.date_this_decade(),
            'ClosingDate': fake.date_this_decade(),
            'AccountStatus': random.choice(['Active', 'Closed']),
            'CurrentBalance': round(random.uniform(1000, 100000), 2),
            'AvailableBalance': round(random.uniform(1000, 100000), 2),
            'OverdraftLimit': round(random.uniform(0, 5000), 2),
            'InterestRate': round(random.uniform(0.5, 5.0), 2),
            'AccountCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'AccountManagerID': random.randint(1, num_records),
            'IsJointAccount': random.choice([True, False]),
            'NomineeName': fake.name(),
            'NomineeRelation': random.choice(['Spouse', 'Child', 'Parent']),
            'LastTransactionDate': fake.date_this_decade(),
            'AccountTier': random.choice(['Standard', 'Gold', 'Platinum'])
        }

        insert_statement = text("""
            INSERT INTO Account_Master (AccountID, AccountNumber, CustomerID, AccountType, BranchCode, 
                                        OpeningDate, ClosingDate, AccountStatus, CurrentBalance, AvailableBalance, 
                                        OverdraftLimit, InterestRate, AccountCurrency, AccountManagerID, 
                                        IsJointAccount, NomineeName, NomineeRelation, LastTransactionDate, AccountTier)
            VALUES (:AccountID, :AccountNumber, :CustomerID, :AccountType, :BranchCode, 
                    :OpeningDate, :ClosingDate, :AccountStatus, :CurrentBalance, :AvailableBalance, 
                    :OverdraftLimit, :InterestRate, :AccountCurrency, :AccountManagerID, 
                    :IsJointAccount, :NomineeName, :NomineeRelation, :LastTransactionDate, :AccountTier)
        """)

        session.execute(insert_statement, account_master_data)
        print(f"Inserted record with AccountID: {account_id}")
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `account_statement` table
def populate_account_statement(num_records):
    for _ in range(num_records):
        account_statement_data = {
            'AccountID': random.randint(1, num_records),
            'StatementDate': fake.date_this_decade(),
            'StatementPeriodStart': fake.date_this_decade(),
            'StatementPeriodEnd': fake.date_this_decade(),
            'OpeningBalance': round(random.uniform(0, 5000), 2),
            'ClosingBalance': round(random.uniform(5000, 20000), 2),
            'TotalCredits': round(random.uniform(0, 10000), 2),
            'TotalDebits': round(random.uniform(0, 10000), 2),
            'InterestEarned': round(random.uniform(0, 1000), 2),
            'ChargesIncurred': round(random.uniform(0, 500), 2),
            'StatementStatus': random.choice(['Completed', 'Pending', 'Failed']),
            'StatementFilePath': fake.file_path(),
        }

        insert_statement = text("""
            INSERT INTO Account_Statements (AccountID, StatementDate, StatementPeriodStart, StatementPeriodEnd, 
                                            OpeningBalance, ClosingBalance, TotalCredits, TotalDebits, 
                                            InterestEarned, ChargesIncurred, StatementStatus, StatementFilePath)
            VALUES (:AccountID, :StatementDate, :StatementPeriodStart, :StatementPeriodEnd, 
                    :OpeningBalance, :ClosingBalance, :TotalCredits, :TotalDebits, 
                    :InterestEarned, :ChargesIncurred, :StatementStatus, :StatementFilePath)
        """)

        session.execute(insert_statement, account_statement_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `loan_applications` table
def populate_loan_applications(num_records):
    for _ in range(num_records):
        loan_application_data = {
            'CustomerID': random.randint(1, num_records),
            'LoanType': random.choice(['Home Loan', 'Auto Loan', 'Personal Loan']),
            'LoanAmount': round(random.uniform(50000, 1000000), 2),
            'ApplicationDate': fake.date_this_year(),
            'ApplicationStatus': random.choice(['Approved', 'Rejected', 'Pending']),
            'ApprovedAmount': round(random.uniform(50000, 1000000), 2) if random.choice([True, False]) else None,
            'ApprovedDate': fake.date_this_year() if random.choice([True, False]) else None,
            'RejectionReason': fake.sentence() if random.choice([True, False]) else None,
            'LoanTermInMonths': random.choice([12, 24, 36, 60]),
            'InterestRate': round(random.uniform(1.0, 15.0), 2),
            'RepaymentSchedule': random.choice(['Monthly', 'Quarterly']),
            'CollateralRequired': random.choice([True, False]),
            'CollateralDetails': fake.sentence(),
            'CreditScore': random.randint(300, 850),
            'ProcessingFee': round(random.uniform(100, 1000), 2),
            'DisbursementDate': fake.date_this_year() if random.choice([True, False]) else None,
            'DisbursedBy': fake.name() if random.choice([True, False]) else None,
            'LoanPurpose': fake.sentence(),
            'RiskGrade': random.choice(['A', 'B', 'C', 'D']),
            'LoanOfficerID': random.randint(1, 10)
        }

        insert_statement = text("""
            INSERT INTO Loan_Applications (CustomerID, LoanType, LoanAmount, ApplicationDate, ApplicationStatus, 
                                           ApprovedAmount, ApprovedDate, RejectionReason, LoanTermInMonths, InterestRate, 
                                           RepaymentSchedule, CollateralRequired, CollateralDetails, CreditScore, 
                                           ProcessingFee, DisbursementDate, DisbursedBy, LoanPurpose, RiskGrade, LoanOfficerID)
            VALUES (:CustomerID, :LoanType, :LoanAmount, :ApplicationDate, :ApplicationStatus, 
                    :ApprovedAmount, :ApprovedDate, :RejectionReason, :LoanTermInMonths, :InterestRate, 
                    :RepaymentSchedule, :CollateralRequired, :CollateralDetails, :CreditScore, 
                    :ProcessingFee, :DisbursementDate, :DisbursedBy, :LoanPurpose, :RiskGrade, :LoanOfficerID)
        """)

        session.execute(insert_statement, loan_application_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `anti_money_laundering_reports` table
def populate_anti_money_laundering_reports(num_records):
    for _ in range(num_records):
        aml_report_data = {
            'CustomerID': random.randint(1, num_records),
            'TransactionID': random.randint(1, num_records),
            'ReportDate': fake.date_this_year(),
            'SuspiciousActivity': fake.sentence(),
            'ReportStatus': random.choice(['Open', 'Investigating', 'Closed']),
            'InvestigationStartDate': fake.date_this_year(),
            'InvestigationEndDate': fake.date_this_year(),
            'RiskScore': random.randint(1, 100),
            'ReportingOfficer': fake.name(),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'EscalationStatus': random.choice(['Escalated', 'Not Escalated']),
            'ReportingDetails': fake.text(),
            'InvestigativeFindings': fake.text(),
            'ResolutionDate': fake.date_this_year(),
            'ResolutionDetails': fake.text(),
            'ReportNotes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Anti_Money_Laundering_Reports (CustomerID, TransactionID, ReportDate, SuspiciousActivity, 
                                                       ReportStatus, InvestigationStartDate, InvestigationEndDate, 
                                                       RiskScore, ReportingOfficer, RegulatoryComplianceStatus, 
                                                       EscalationStatus, ReportingDetails, InvestigativeFindings, 
                                                       ResolutionDate, ResolutionDetails, ReportNotes)
            VALUES (:CustomerID, :TransactionID, :ReportDate, :SuspiciousActivity, :ReportStatus, :InvestigationStartDate, 
                    :InvestigationEndDate, :RiskScore, :ReportingOfficer, :RegulatoryComplianceStatus, 
                    :EscalationStatus, :ReportingDetails, :InvestigativeFindings, :ResolutionDate, :ResolutionDetails, 
                    :ReportNotes)
        """)

        session.execute(insert_statement, aml_report_data)

# Function to populate the `loan_collateral_details` table
def populate_loan_collateral_details(num_records):
    for _ in range(num_records):
        collateral_data = {
            'LoanAccountID': random.randint(1, num_records),
            'CollateralType': random.choice(['Property', 'Vehicle', 'Jewelry']),
            'CollateralValue': round(random.uniform(50000, 1000000), 2),
            'CollateralStatus': random.choice(['Pledged', 'Released']),
            'AppraisalDate': fake.date_this_year(),
            'RiskAssessmentScore': random.randint(1, 100),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO loan_collateral_details (LoanAccountID, CollateralType, CollateralValue, CollateralStatus, 
                                                 AppraisalDate, RiskAssessmentScore, Notes)
            VALUES (:LoanAccountID, :CollateralType, :CollateralValue, :CollateralStatus, :AppraisalDate, 
                    :RiskAssessmentScore, :Notes)
        """)

        session.execute(insert_statement, collateral_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `audit_logs` table
def date_next_year():
    today = datetime.today()
    next_year = today.replace(year=today.year + 1)
    return next_year.date()

def populate_audit_logs(num_records):
    for _ in range(num_records):
        audit_log_data = {
            'AuditDate': fake.date_this_year(),
            'AuditType': random.choice(['Internal', 'External', 'Regulatory']),
            'AuditedEntity': random.choice(['Account', 'Transaction', 'Customer']),
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'TransactionID': random.randint(1, num_records),
            'Auditor': fake.name(),
            'AuditStatus': random.choice(['Completed', 'Pending', 'Escalated']),
            'Findings': fake.sentence(),
            'ComplianceCheckStatus': random.choice(['Passed', 'Failed']),
            'CorrectiveActions': fake.sentence(),
            'EscalationStatus': random.choice(['Escalated', 'Not Escalated']),
            'FinalReportDate': date_next_year(),
            'FinalReportDetails': fake.text(),
            'ResolutionStatus': random.choice(['Resolved', 'Unresolved']),
            'ResolutionDate': date_next_year(),
            'ResolutionDetails': fake.text(),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Audit_Logs (AuditDate, AuditType, AuditedEntity, CustomerID, AccountID, TransactionID, Auditor, 
                                    AuditStatus, Findings, ComplianceCheckStatus, CorrectiveActions, EscalationStatus, 
                                    FinalReportDate, FinalReportDetails, ResolutionStatus, ResolutionDate, ResolutionDetails, 
                                    Notes)
            VALUES (:AuditDate, :AuditType, :AuditedEntity, :CustomerID, :AccountID, :TransactionID, :Auditor, 
                    :AuditStatus, :Findings, :ComplianceCheckStatus, :CorrectiveActions, :EscalationStatus, 
                    :FinalReportDate, :FinalReportDetails, :ResolutionStatus, :ResolutionDate, :ResolutionDetails, 
                    :Notes)
        """)

        session.execute(insert_statement, audit_log_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `loan_defaults` table
def populate_loan_defaults(num_records):
    for _ in range(num_records):
        loan_default_data = {
            'LoanAccountID': random.randint(1, num_records),
            'DefaultDate': fake.date_this_year(),
            'OutstandingAmount': round(random.uniform(5000, 50000), 2),
            'LastPaymentDate': fake.date_this_year(),
            'DefaultStatus': random.choice(['Open', 'Resolved']),
            'CollectionAgency': fake.company(),
            'CollectionAgencyContact': fake.name(),
            'CollectionAttempts': random.randint(1, 10),
            'RecoveryAmount': round(random.uniform(1000, 25000), 2),
            'RecoveryDate': date_next_year(),
            'LegalActionStatus': random.choice(['Initiated', 'Not Initiated']),
            'LegalActionDetails': fake.text(),
            'RiskMitigationStrategy': fake.sentence(),
            'DefaultReason': fake.sentence(),
            'IsLoanRestructured': random.choice([True, False]),
            'RestructuredTerms': fake.text(),
            'RestructuredAmount': round(random.uniform(1000, 25000), 2),
            'RestructuredDate': date_next_year(),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Loan_Defaults (LoanAccountID, DefaultDate, OutstandingAmount, LastPaymentDate, DefaultStatus, 
                                      CollectionAgency, CollectionAgencyContact, CollectionAttempts, RecoveryAmount, 
                                      RecoveryDate, LegalActionStatus, LegalActionDetails, RiskMitigationStrategy, 
                                      DefaultReason, IsLoanRestructured, RestructuredTerms, RestructuredAmount, 
                                      RestructuredDate, Notes)
            VALUES (:LoanAccountID, :DefaultDate, :OutstandingAmount, :LastPaymentDate, :DefaultStatus, 
                    :CollectionAgency, :CollectionAgencyContact, :CollectionAttempts, :RecoveryAmount, 
                    :RecoveryDate, :LegalActionStatus, :LegalActionDetails, :RiskMitigationStrategy, 
                    :DefaultReason, :IsLoanRestructured, :RestructuredTerms, :RestructuredAmount, 
                    :RestructuredDate, :Notes)
        """)

        session.execute(insert_statement, loan_default_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `bank_charges` table
def populate_bank_charges(num_records):
    for _ in range(num_records):
        bank_charge_data = {
            'ChargeType': random.choice(['Account Maintenance', 'Late Payment', 'Transaction Fee']),
            'ChargeDescription': fake.sentence(),
            'Amount': round(random.uniform(10, 500), 2),
            'ApplicableTo': random.choice(['Savings Account', 'Fixed Deposit']),
            'Frequency': random.choice(['Monthly', 'Annually']),
            'ChargeDate': fake.date_this_year(),
            'ChargeStatus': random.choice(['Applied', 'Waived']),
            'TaxAmount': round(random.uniform(5, 50), 2),
            'TotalChargeAmount': round(random.uniform(15, 550), 2),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'ApprovedBy': fake.name(),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO bank_charges (ChargeType, ChargeDescription, Amount, ApplicableTo, Frequency, ChargeDate, 
                                      ChargeStatus, TaxAmount, TotalChargeAmount, RegulatoryComplianceStatus, ApprovedBy, Notes)
            VALUES (:ChargeType, :ChargeDescription, :Amount, :ApplicableTo, :Frequency, :ChargeDate, 
                    :ChargeStatus, :TaxAmount, :TotalChargeAmount, :RegulatoryComplianceStatus, :ApprovedBy, :Notes)
        """)

        session.execute(insert_statement, bank_charge_data)

# Function to populate the `loan_interest_details` table
def populate_loan_interest_details(num_records):
    for _ in range(num_records):
        loan_interest_data = {
            'LoanAccountID': random.randint(1, num_records),
            'InterestType': random.choice(['Fixed', 'Variable']),
            'InterestRate': round(random.uniform(3.5, 12.5), 2),
            'EffectiveDate': fake.date_this_year(),
            'ExpiryDate': date_next_year(),
            'RateChangeFrequency': random.choice(['Monthly', 'Quarterly', 'Annually']),
            'RateMargin': round(random.uniform(0.5, 5.0), 2),
            'BaseRate': round(random.uniform(1.0, 3.0), 2),
            'PenaltyRate': round(random.uniform(0.5, 5.0), 2),
            'RiskAdjustedRate': round(random.uniform(3.5, 12.5), 2),
            'IsRateCapped': random.choice([True, False]),
            'RateCap': round(random.uniform(5.0, 15.0), 2),
            'RateFloor': round(random.uniform(1.0, 3.0), 2),
            'AnnualPercentageRate': round(random.uniform(3.5, 12.5), 2),
            'InterestCompoundingFrequency': random.choice(['Monthly', 'Quarterly']),
            'RateHistory': fake.text(),
            'RateChangeApprovalStatus': random.choice(['Approved', 'Pending', 'Rejected']),
            'ApprovedBy': fake.name(),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Loan_Interest_Rates (LoanAccountID, InterestType, InterestRate, EffectiveDate, ExpiryDate, 
                                             RateChangeFrequency, RateMargin, BaseRate, PenaltyRate, RiskAdjustedRate, 
                                             IsRateCapped, RateCap, RateFloor, AnnualPercentageRate, 
                                             InterestCompoundingFrequency, RateHistory, RateChangeApprovalStatus, 
                                             ApprovedBy, Notes)
            VALUES (:LoanAccountID, :InterestType, :InterestRate, :EffectiveDate, :ExpiryDate, 
                    :RateChangeFrequency, :RateMargin, :BaseRate, :PenaltyRate, :RiskAdjustedRate, 
                    :IsRateCapped, :RateCap, :RateFloor, :AnnualPercentageRate, 
                    :InterestCompoundingFrequency, :RateHistory, :RateChangeApprovalStatus, 
                    :ApprovedBy, :Notes)
        """)

        session.execute(insert_statement, loan_interest_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `branch_details` table
def populate_branch_details(num_records):
    for _ in range(num_records):
        branch_data = {
            'BranchCode': fake.bban(),
            'BranchName': fake.company(),
            'BranchAddress': fake.address(),
            'BranchPhoneNumber': fake.phone_number(),
            'BranchManager': fake.name(),
            'Region': random.choice(['North', 'South', 'East', 'West']),
            'OperatingHours': f"{random.randint(8, 10)} AM - {random.randint(5, 7)} PM",
            'NumberOfEmployees': random.randint(10, 100),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'LastAuditDate': fake.date_this_year(),
            'RiskAssessmentScore': random.randint(1, 100),
            'CustomerServiceRating': round(random.uniform(1.0, 5.0), 1),
            'NumberOfAccounts': random.randint(100, 1000),
            'BranchEmail': fake.email(),
            'BranchStatus': random.choice(['Open', 'Closed'])
        }

        insert_statement = text("""
            INSERT INTO branch_details (BranchCode, BranchName, BranchAddress, BranchPhoneNumber, BranchManager, Region, 
                                        OperatingHours, NumberOfEmployees, RegulatoryComplianceStatus, LastAuditDate, 
                                        RiskAssessmentScore, CustomerServiceRating, NumberOfAccounts, BranchEmail, BranchStatus)
            VALUES (:BranchCode, :BranchName, :BranchAddress, :BranchPhoneNumber, :BranchManager, :Region, 
                    :OperatingHours, :NumberOfEmployees, :RegulatoryComplianceStatus, :LastAuditDate, 
                    :RiskAssessmentScore, :CustomerServiceRating, :NumberOfAccounts, :BranchEmail, :BranchStatus)
        """)

        session.execute(insert_statement, branch_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `loan_repayment_schedules` table
def populate_loan_repayment_schedules(num_records):
    for _ in range(num_records):
        repayment_schedule_data = {
            'LoanAccountID': random.randint(1, num_records),
            'PaymentDueDate': fake.date_this_year(),
            'PrincipalAmountDue': round(random.uniform(450, 4500), 2),
            'InterestAmountDue': round(random.uniform(50, 500), 2),
            'PenaltyAmountDue': round(random.uniform(50, 500), 2),
            'TotalAmountDue': round(random.uniform(500, 5000), 2),
            'PaymentStatus': random.choice(['Paid', 'Pending', 'Overdue']),
            'PaymentDate': fake.date_this_year(),
            'PaymentAmount': round(random.uniform(500, 5000), 2),
            'LateFee': round(random.uniform(10, 100), 2),
            'PaymentMethod': random.choice(['Cash', 'Credit Card', 'Bank Transfer']),
            'ReferenceNumber': fake.bban(),
            'RemainingBalance': round(random.uniform(0, 5000), 2),
            'InstallmentNumber': random.randint(1, 36),
            'IsGracePeriod': random.choice([True, False]),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Loan_Repayment_Schedules (LoanAccountID, PaymentDueDate, PrincipalAmountDue, InterestAmountDue, 
                                                  PenaltyAmountDue, TotalAmountDue, PaymentStatus, PaymentDate, 
                                                  PaymentAmount, LateFee, PaymentMethod, ReferenceNumber, 
                                                  RemainingBalance, InstallmentNumber, IsGracePeriod, Notes)
            VALUES (:LoanAccountID, :PaymentDueDate, :PrincipalAmountDue, :InterestAmountDue, :PenaltyAmountDue, 
                    :TotalAmountDue, :PaymentStatus, :PaymentDate, :PaymentAmount, :LateFee, :PaymentMethod, 
                    :ReferenceNumber, :RemainingBalance, :InstallmentNumber, :IsGracePeriod, :Notes)
        """)

        session.execute(insert_statement, repayment_schedule_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `cheque_clearing` table
def populate_cheque_clearing(num_records):
    for _ in range(num_records):
        cheque_clearing_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'ChequeNumber': fake.bban(),
            'ChequeDate': fake.date_this_year(),
            'ChequeAmount': round(random.uniform(100, 5000), 2),
            'ChequeCurrency': fake.currency_code(),
            'PayeeName': fake.name(),
            'PayeeAccountNumber': fake.bban(),
            'PayeeBankName': fake.company(),
            'PayeeBankBranchCode': fake.bban(),
            'ChequeStatus': random.choice(['Cleared', 'Bounced', 'Hold']),
            'ClearingDate': fake.date_this_year(),
            'ClearingReferenceNumber': fake.bban(),
            'TransactionID': random.randint(1, num_records),
            'RiskAssessmentScore': random.randint(1, 100),
            'ReasonForBouncing': fake.sentence(),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Cheque_Clearing (CustomerID, AccountID, ChequeNumber, ChequeDate, ChequeAmount, ChequeCurrency, 
                                         PayeeName, PayeeAccountNumber, PayeeBankName, PayeeBankBranchCode, ChequeStatus, 
                                         ClearingDate, ClearingReferenceNumber, TransactionID, RiskAssessmentScore, 
                                         ReasonForBouncing, Notes)
            VALUES (:CustomerID, :AccountID, :ChequeNumber, :ChequeDate, :ChequeAmount, :ChequeCurrency, 
                    :PayeeName, :PayeeAccountNumber, :PayeeBankName, :PayeeBankBranchCode, :ChequeStatus, 
                    :ClearingDate, :ClearingReferenceNumber, :TransactionID, :RiskAssessmentScore, 
                    :ReasonForBouncing, :Notes)
        """)

        session.execute(insert_statement, cheque_clearing_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `mortgage_accounts` table
def populate_mortgage_accounts(num_records):
    for _ in range(num_records):
        insurance_expiry_date = fake.date_this_year()
        next_year_date = (insurance_expiry_date + timedelta(days=365)).strftime('%Y-%m-%d')
        
        mortgage_account_data = {
            'CustomerID': random.randint(1, num_records),
            'ApplicationID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'PropertyValue': round(random.uniform(100000, 1000000), 2),
            'LoanAmount': round(random.uniform(50000, 800000), 2),
            'InterestRate': round(random.uniform(2.5, 5.5), 2),
            'LoanTermInYears': random.choice([10, 20, 30]),
            'RepaymentSchedule': random.choice(['Monthly', 'Quarterly']),
            'MortgageStatus': random.choice(['Active', 'Closed', 'Defaulted']),
            'CollateralDetails': fake.sentence(),
            'PropertyAddress': fake.address(),
            'PropertyType': random.choice(['Residential', 'Commercial']),
            'LienStatus': random.choice(['First Lien', 'Second Lien']),
            'RiskGrade': random.choice(['A', 'B', 'C', 'D']),
            'AppraisalValue': round(random.uniform(100000, 1000000), 2),
            'AppraisalDate': fake.date_this_decade(),
            'InsuranceAmount': round(random.uniform(1000, 10000), 2),
            'InsuranceExpiryDate': next_year_date,
            'MortgageOfficerID': random.randint(1, num_records)
        }

        insert_statement = text("""
            INSERT INTO Mortgage_Accounts (CustomerID, ApplicationID, AccountNumber, PropertyValue, LoanAmount, InterestRate, 
                                           LoanTermInYears, RepaymentSchedule, MortgageStatus, CollateralDetails, PropertyAddress, 
                                           PropertyType, LienStatus, RiskGrade, AppraisalValue, AppraisalDate, InsuranceAmount, 
                                           InsuranceExpiryDate, MortgageOfficerID)
            VALUES (:CustomerID, :ApplicationID, :AccountNumber, :PropertyValue, :LoanAmount, :InterestRate, 
                    :LoanTermInYears, :RepaymentSchedule, :MortgageStatus, :CollateralDetails, :PropertyAddress, 
                    :PropertyType, :LienStatus, :RiskGrade, :AppraisalValue, :AppraisalDate, :InsuranceAmount, 
                    :InsuranceExpiryDate, :MortgageOfficerID)
        """)

        session.execute(insert_statement, mortgage_account_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `commercial_lending` table
def populate_commercial_lending(num_records):
    for _ in range(num_records):
        commercial_lending_data = {
            'CorporateAccountID': random.randint(1, num_records),
            'LoanType': random.choice(['Working Capital', 'Term Loan']),
            'LoanAmount': round(random.uniform(100000, 5000000), 2),
            'DisbursementDate': fake.date_this_decade(),
            'RepaymentTermInMonths': random.choice([12, 24, 36, 60]),
            'InterestRate': round(random.uniform(3.5, 8.5), 2),
            'RepaymentSchedule': random.choice(['Monthly', 'Quarterly']),
            'LoanStatus': random.choice(['Active', 'Closed', 'Defaulted']),
            'CollateralDetails': fake.sentence(),
            'RiskAssessmentScore': random.randint(1, 100),
            'GracePeriodInMonths': random.choice([0, 6, 12]),
            'PenaltyForLatePayment': round(random.uniform(100, 1000), 2),
            'EarlyRepaymentPenalty': round(random.uniform(100, 1000), 2),
            'LoanOfficer': fake.name(),
            'LoanPurpose': fake.sentence(),
            'RegulatoryComplianceStatus': random.choice(['Passed', 'Failed']),
            'CreditRating': random.choice(['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC', 'CC', 'C']),
            'AccountManagerID': random.randint(1, num_records),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Commercial_Lending (CorporateAccountID, LoanType, LoanAmount, DisbursementDate, RepaymentTermInMonths, 
                                           InterestRate, RepaymentSchedule, LoanStatus, CollateralDetails, RiskAssessmentScore, 
                                           GracePeriodInMonths, PenaltyForLatePayment, EarlyRepaymentPenalty, LoanOfficer, 
                                           LoanPurpose, RegulatoryComplianceStatus, CreditRating, AccountManagerID, Notes)
            VALUES (:CorporateAccountID, :LoanType, :LoanAmount, :DisbursementDate, :RepaymentTermInMonths, :InterestRate, 
                    :RepaymentSchedule, :LoanStatus, :CollateralDetails, :RiskAssessmentScore, :GracePeriodInMonths, 
                    :PenaltyForLatePayment, :EarlyRepaymentPenalty, :LoanOfficer, :LoanPurpose, :RegulatoryComplianceStatus, 
                    :CreditRating, :AccountManagerID, :Notes)
        """)

        session.execute(insert_statement, commercial_lending_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `overdraft_accounts` table
def populate_overdraft_accounts(num_records):
    for _ in range(num_records):
        overdraft_end_date = fake.date_this_year() + timedelta(days=365)
        overdraft_account_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'ApprovedLimit': round(random.uniform(5000, 50000), 2),
            'CurrentOverdraftBalance': round(random.uniform(1000, 30000), 2),
            'InterestRate': round(random.uniform(5.0, 15.0), 2),
            'OverdraftStartDate': fake.date_this_year(),
            'OverdraftEndDate': overdraft_end_date.strftime('%Y-%m-%d'),
            'OverdraftStatus': random.choice(['Active', 'Inactive']),
            'FeeAmount': round(random.uniform(10, 100), 2),
            'PenaltyRate': round(random.uniform(1.0, 5.0), 2),
            'NextReviewDate': fake.date_this_year(),
            'RiskAssessmentScore': random.randint(1, 100),
            'CollateralDetails': fake.sentence(),
            'CreditScore': random.randint(300, 850),
            'OverdraftOfficerID': random.randint(1, num_records),
            'IsSecured': random.choice([True, False]),
            'CollateralID': random.randint(1, num_records)
        }

        insert_statement = text("""
            INSERT INTO Overdraft_Accounts (CustomerID, AccountNumber, ApprovedLimit, CurrentOverdraftBalance, InterestRate, 
                                            OverdraftStartDate, OverdraftEndDate, OverdraftStatus, FeeAmount, PenaltyRate, 
                                            NextReviewDate, RiskAssessmentScore, CollateralDetails, CreditScore, 
                                            OverdraftOfficerID, IsSecured, CollateralID)
            VALUES (:CustomerID, :AccountNumber, :ApprovedLimit, :CurrentOverdraftBalance, :InterestRate, 
                    :OverdraftStartDate, :OverdraftEndDate, :OverdraftStatus, :FeeAmount, :PenaltyRate, 
                    :NextReviewDate, :RiskAssessmentScore, :CollateralDetails, :CreditScore, 
                    :OverdraftOfficerID, :IsSecured, :CollateralID)
        """)

        session.execute(insert_statement, overdraft_account_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `compliance_logs` table
def populate_compliance_logs(num_records):
    for _ in range(num_records):
        resolution_date = fake.date_this_year() + timedelta(days=365)
        compliance_log_data = {
            'LogDate': fake.date_this_year(),
            'LogType': random.choice(['AML Check', 'KYC Check', 'Regulatory Audit']),
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'TransactionID': random.randint(1, num_records),
            'ComplianceStatus': random.choice(['Passed', 'Failed', 'Under Review']),
            'ComplianceDetails': fake.text(),
            'RegulatoryApprovalStatus': random.choice(['Approved', 'Pending', 'Rejected']),
            'ReportingOfficer': fake.name(),
            'EscalationStatus': random.choice(['Escalated', 'Not Escalated']),
            'InvestigationDetails': fake.text(),
            'ResolutionStatus': random.choice(['Resolved', 'Unresolved']),
            'ResolutionDate': resolution_date.strftime('%Y-%m-%d'),
            'ResolutionDetails': fake.text(),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Compliance_Logs (LogDate, LogType, CustomerID, AccountID, TransactionID, ComplianceStatus, 
                                         ComplianceDetails, RegulatoryApprovalStatus, ReportingOfficer, EscalationStatus, 
                                         InvestigationDetails, ResolutionStatus, ResolutionDate, ResolutionDetails, Notes)
            VALUES (:LogDate, :LogType, :CustomerID, :AccountID, :TransactionID, :ComplianceStatus, 
                    :ComplianceDetails, :RegulatoryApprovalStatus, :ReportingOfficer, :EscalationStatus, 
                    :InvestigationDetails, :ResolutionStatus, :ResolutionDate, :ResolutionDetails, :Notes)
        """)

        session.execute(insert_statement, compliance_log_data)
    
    session.commit()
    print("All records inserted successfully.")

def populate_payment_instructions(num_records):
    for _ in range(num_records):
        payment_instruction_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'PaymentAmount': round(random.uniform(100, 10000), 2),
            'PaymentDate': fake.date_this_year(),
            'PaymentStatus': random.choice(['Scheduled', 'Executed', 'Cancelled']),
            'PaymentMethod': random.choice(['Bank Transfer', 'Credit Card']),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'ReferenceNumber': fake.bban(),
            'PurposeOfPayment': fake.sentence(),
            'PaymentCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'ScheduledPaymentDate': fake.date_this_year(),
            'RecurrencePattern': random.choice(['Monthly', 'Quarterly']),
            'NextPaymentDate': fake.date_this_year(),
            'InstructionSource': random.choice(['Online', 'In-branch']),
            'PaymentChannel': random.choice(['Mobile', 'Web']),
            'TransactionID': random.randint(1, num_records),
            'RiskAssessmentScore': random.randint(1, 100),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Payment_Instructions (CustomerID, AccountID, PaymentAmount, PaymentDate, PaymentStatus, 
                                              PaymentMethod, BeneficiaryName, BeneficiaryAccountNumber, 
                                              BeneficiaryBankName, BeneficiaryBankSWIFT, ReferenceNumber, 
                                              PurposeOfPayment, PaymentCurrency, ScheduledPaymentDate, 
                                              RecurrencePattern, NextPaymentDate, InstructionSource, 
                                              PaymentChannel, TransactionID, RiskAssessmentScore, Notes)
            VALUES (:CustomerID, :AccountID, :PaymentAmount, :PaymentDate, :PaymentStatus, :PaymentMethod, 
                    :BeneficiaryName, :BeneficiaryAccountNumber, :BeneficiaryBankName, :BeneficiaryBankSWIFT, 
                    :ReferenceNumber, :PurposeOfPayment, :PaymentCurrency, :ScheduledPaymentDate, 
                    :RecurrencePattern, :NextPaymentDate, :InstructionSource, :PaymentChannel, :TransactionID, 
                    :RiskAssessmentScore, :Notes)
        """)

        session.execute(insert_statement, payment_instruction_data)
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `contact_details` table

def populate_contact_details(num_records):
    # Get the maximum ContactID from the database to avoid duplicates
    max_contact_id = session.execute(select(func.max(text('ContactID'))).select_from(text('Customer_Contact_Details'))).scalar() or 0
    contact_id_counter = max_contact_id + 1  # Start from the next available ID

    for _ in range(num_records):
        valid_from_date = fake.date_this_decade()
        valid_to_date = (valid_from_date + timedelta(days=365)).strftime('%Y-%m-%d')

        contact_type = random.choice(['Email', 'Phone', 'Postal'])
        if contact_type == 'Email':
            contact_detail = fake.email()
        elif contact_type == 'Phone':
            contact_detail = fake.phone_number()
        else:
            contact_detail = fake.address()

        contact_details_data = {
            'ContactID': contact_id_counter,
            'CustomerID': random.randint(1, num_records),
            'ContactType': contact_type,
            'ContactDetail': contact_detail,
            'IsPrimaryContact': fake.boolean(),
            'ValidFrom': valid_from_date,
            'ValidTo': valid_to_date,
        }

        insert_statement = text("""
            INSERT INTO Customer_Contact_Details (ContactID, CustomerID, ContactType, ContactDetail, IsPrimaryContact, ValidFrom, ValidTo)
            VALUES (:ContactID, :CustomerID, :ContactType, :ContactDetail, :IsPrimaryContact, :ValidFrom, :ValidTo)
        """)

        session.execute(insert_statement, contact_details_data)
        contact_id_counter += 1  # Increment the counter for the next record
    
    session.commit()
    print("All records inserted successfully.")

# Function to populate the `regulatory_reports` table
def populate_regulatory_reports(num_records):
    for _ in range(num_records):
        regulatory_report_data = {
            'ReportType': random.choice(['AML Report', 'KYC Report', 'Tax Report']),
            'ReportingPeriodStartDate': fake.date_this_year(),
            'ReportingPeriodEndDate': fake.date_this_year(),
            'SubmissionDate': fake.date_this_year(),
            'ReportStatus': random.choice(['Submitted', 'Pending', 'Rejected']),
            'RegulatoryBody': random.choice(['FATF', 'FINRA', 'SEC']),
            'ReportedBy': fake.name(),
            'ComplianceStatus': random.choice(['Compliant', 'Non-Compliant']),
            'RiskAssessmentScore': random.randint(1, 100),
            'ReportDetails': fake.text(),
            'CorrectiveActions': fake.sentence(),
            'ApprovalStatus': random.choice(['Approved', 'Pending', 'Rejected']),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Regulatory_Reports (ReportType, ReportingPeriodStartDate, ReportingPeriodEndDate, SubmissionDate, ReportStatus, 
                                            RegulatoryBody, ReportedBy, ComplianceStatus, RiskAssessmentScore, ReportDetails, 
                                            CorrectiveActions, ApprovalStatus, Notes)
            VALUES (:ReportType, :ReportingPeriodStartDate, :ReportingPeriodEndDate, :SubmissionDate, :ReportStatus, 
                    :RegulatoryBody, :ReportedBy, :ComplianceStatus, :RiskAssessmentScore, :ReportDetails, 
                    :CorrectiveActions, :ApprovalStatus, :Notes)
        """)

        session.execute(insert_statement, regulatory_report_data)

def random_datetime_this_year():
    """Generate a random datetime within the current year."""
    start = datetime(datetime.now().year, 1, 1)
    end = datetime(datetime.now().year + 1, 1, 1)
    return fake.date_time_between(start_date=start, end_date=end)

# Function to populate the `corporate_accounts` table
def populate_corporate_accounts(num_records):
    for _ in range(num_records):
        account_opening_date = random_datetime_this_year()
        account_closure_date = account_opening_date + timedelta(days=random.randint(365, 1825)) if random.choice([True, False]) else None

        corporate_account_data = {
            'CompanyName': fake.company(),
            'AccountNumber': fake.bban(),
            'AccountType': random.choice(['Checking', 'Savings', 'Fixed Deposit']),
            'AccountStatus': random.choice(['Active', 'Dormant', 'Closed']),
            'BranchCode': fake.bban()[:10],  # Example BranchCode
            'AccountOpeningDate': account_opening_date,
            'AccountManagerID': random.randint(1, num_records),
            'AuthorizedSignatories': fake.name(),
            'TaxID': fake.ssn(),
            'RiskAssessmentScore': random.randint(1, 100),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Corporate_Accounts (CompanyName, AccountNumber, AccountType, AccountStatus, BranchCode, 
                                            AccountOpeningDate, AccountManagerID, AuthorizedSignatories, TaxID, 
                                            RiskAssessmentScore, Notes)
            VALUES (:CompanyName, :AccountNumber, :AccountType, :AccountStatus, :BranchCode, :AccountOpeningDate, 
                    :AccountManagerID, :AuthorizedSignatories, :TaxID, :RiskAssessmentScore, :Notes)
        """)

        session.execute(insert_statement, corporate_account_data)
        print(f"Inserted record for {corporate_account_data['CompanyName']}")


# Function to populate the `risk_exposure` table
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def date_next_year():
    return datetime.now() + timedelta(days=365)

def populate_risk_exposure(num_records):
    for _ in range(num_records):
        risk_exposure_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'ExposureDate': fake.date_this_year(),
            'RiskType': random.choice(['Credit Risk', 'Liquidity Risk', 'Market Risk']),
            'RiskScore': random.randint(1, 100),
            'RiskMitigationStrategy': fake.sentence(),
            'ExposureAmount': round(random.uniform(1000, 1000000), 2),
            'ExposureCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'ExposureStatus': random.choice(['Active', 'Resolved', 'Escalated']),
            'ResolutionDate': fake.date_this_year(),
            'ResolutionDetails': fake.text(),
            'RiskOfficer': fake.name(),
            'ComplianceCheckStatus': random.choice(['Passed', 'Failed']),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Risk_Exposure (CustomerID, AccountID, ExposureDate, RiskType, RiskScore, RiskMitigationStrategy, 
                                       ExposureAmount, ExposureCurrency, ExposureStatus, ResolutionDate, ResolutionDetails, 
                                       RiskOfficer, ComplianceCheckStatus, Notes)
            VALUES (:CustomerID, :AccountID, :ExposureDate, :RiskType, :RiskScore, :RiskMitigationStrategy, 
                    :ExposureAmount, :ExposureCurrency, :ExposureStatus, :ResolutionDate, :ResolutionDetails, 
                    :RiskOfficer, :ComplianceCheckStatus, :Notes)
        """)

        session.execute(insert_statement, risk_exposure_data)
        print(f"Inserted risk exposure record for CustomerID {risk_exposure_data['CustomerID']}")

# Function to populate the `credit_score_reports` table
from faker import Faker
import random
from datetime import datetime
from sqlalchemy.sql import text

fake = Faker()

def populate_credit_score_reports(num_records):
    for _ in range(num_records):
        credit_score_report_data = {
            'CustomerID': random.randint(1, num_records),
            'CreditScore': random.randint(300, 850),
            'ReportDate': fake.date_this_year(),
            'CreditBureau': random.choice(['Equifax', 'Experian', 'TransUnion']),
            'ReportSummary': fake.text(),
            'TotalDebt': round(random.uniform(1000, 50000), 2),
            'PaymentHistoryScore': random.randint(300, 850),
            'DebtToIncomeRatio': round(random.uniform(0, 100), 2),
            'NumberOfOpenAccounts': random.randint(0, 10),
            'NumberOfClosedAccounts': random.randint(0, 10),
            'CreditUtilizationRate': round(random.uniform(0, 100), 2),
            'DerogatoryMarks': random.randint(0, 5),
            'RecentInquiries': random.randint(0, 5),
            'PublicRecords': random.randint(0, 3),
            'AccountAgeInMonths': random.randint(0, 240),
            'LoanRepaymentHistory': fake.text(max_nb_chars=255),
            'OverdraftHistory': fake.text(max_nb_chars=255),
            'CreditCardUsageHistory': fake.text(max_nb_chars=255),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Credit_Score_Reports (CustomerID, CreditScore, ReportDate, CreditBureau, ReportSummary, 
                                              TotalDebt, PaymentHistoryScore, DebtToIncomeRatio, NumberOfOpenAccounts, 
                                              NumberOfClosedAccounts, CreditUtilizationRate, DerogatoryMarks, 
                                              RecentInquiries, PublicRecords, AccountAgeInMonths, LoanRepaymentHistory, 
                                              OverdraftHistory, CreditCardUsageHistory, Notes)
            VALUES (:CustomerID, :CreditScore, :ReportDate, :CreditBureau, :ReportSummary, 
                    :TotalDebt, :PaymentHistoryScore, :DebtToIncomeRatio, :NumberOfOpenAccounts, 
                    :NumberOfClosedAccounts, :CreditUtilizationRate, :DerogatoryMarks, 
                    :RecentInquiries, :PublicRecords, :AccountAgeInMonths, :LoanRepaymentHistory, 
                    :OverdraftHistory, :CreditCardUsageHistory, :Notes)
        """)

        session.execute(insert_statement, credit_score_report_data)
        print(f"Inserted credit score report record for CustomerID {credit_score_report_data['CustomerID']}")

# Function to populate the `savings_account` table
def populate_savings_account(num_records):
    for _ in range(num_records):
        savings_account_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.bban(),
            'BranchCode': fake.swift11(),  # Assuming BranchCode is a string similar to SWIFT/BIC
            'AccountBalance': round(random.uniform(1000, 100000), 2),
            'InterestRate': round(random.uniform(1.5, 4.5), 2),
            'MinimumBalance': round(random.uniform(100, 500), 2),
            'PenaltyForBelowMinBalance': round(random.uniform(10, 50), 2),
            'LastTransactionDate': fake.date_this_year(),
            'OverdraftFacility': random.choice([True, False]),
            'OverdraftLimit': round(random.uniform(1000, 10000), 2),
            'AccountTier': random.choice(['Regular', 'Premium']),
            'AccountType': random.choice(['Savings', 'Checking']),
            'NomineeName': fake.name(),
            'NomineeRelation': random.choice(['Spouse', 'Child', 'Parent']),
            'AccountOpeningDate': fake.date_this_decade(),
            'AccountClosureDate': fake.date_this_decade() if random.choice([True, False]) else None,
            'AccountManagerID': random.randint(1, num_records),
            'TransactionLimitPerDay': round(random.uniform(1000, 10000), 2),
            'Notes': fake.text()
        }

        insert_statement = text("""
            INSERT INTO Savings_Accounts (CustomerID, AccountNumber, BranchCode, AccountBalance, InterestRate, 
                                          MinimumBalance, PenaltyForBelowMinBalance, LastTransactionDate, 
                                          OverdraftFacility, OverdraftLimit, AccountTier, AccountType, NomineeName, 
                                          NomineeRelation, AccountOpeningDate, AccountClosureDate, AccountManagerID, 
                                          TransactionLimitPerDay, Notes)
            VALUES (:CustomerID, :AccountNumber, :BranchCode, :AccountBalance, :InterestRate, :MinimumBalance, 
                    :PenaltyForBelowMinBalance, :LastTransactionDate, :OverdraftFacility, :OverdraftLimit, :AccountTier, 
                    :AccountType, :NomineeName, :NomineeRelation, :AccountOpeningDate, :AccountClosureDate, 
                    :AccountManagerID, :TransactionLimitPerDay, :Notes)
        """)

        session.execute(insert_statement, savings_account_data)
        print(f"Inserted savings account record")

def date_next_month():
    today = date.today()
    next_month = today.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)
# Function to populate the `creditcard_accounts` table
def populate_creditcard_accounts(num_records):
    for _ in range(num_records):
        creditcard_account_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': fake.credit_card_number(),
            'CreditLimit': round(random.uniform(5000, 50000), 2),
            'AvailableCredit': round(random.uniform(1000, 20000), 2),
            'InterestRate': round(random.uniform(10.0, 25.0), 2),
            'AnnualFee': round(random.uniform(50, 500), 2),
            'DueDate': date_next_month(),
            'MinimumPayment': round(random.uniform(50, 500), 2),
            'LateFee': round(random.uniform(10, 100), 2),
            'CardStatus': random.choice(['Active', 'Suspended', 'Closed']),
            'CardType': random.choice(['Visa', 'MasterCard']),
            'ExpiryDate': fake.date_this_decade(),
            'RiskAssessmentScore': random.randint(1, 100),
            'LastPaymentDate': fake.date_this_year(),
            'LastPaymentAmount': round(random.uniform(50, 1000), 2),
            'BillingCycle': random.choice(['Monthly', 'Quarterly']),
            'CreditCardIssuer': fake.company(),
            'CreditCardOfficerID': random.randint(1, num_records),
            'CreatedAt': datetime.now(),
            'UpdatedAt': datetime.now()
        }

        insert_statement = text("""
            INSERT INTO Credit_Card_Accounts (CustomerID, AccountNumber, CreditLimit, AvailableCredit, InterestRate, AnnualFee, 
                                              DueDate, MinimumPayment, LateFee, CardStatus, CardType, ExpiryDate, 
                                              RiskAssessmentScore, LastPaymentDate, LastPaymentAmount, BillingCycle, 
                                              CreditCardIssuer, CreditCardOfficerID, CreatedAt, UpdatedAt)
            VALUES (:CustomerID, :AccountNumber, :CreditLimit, :AvailableCredit, :InterestRate, :AnnualFee, 
                    :DueDate, :MinimumPayment, :LateFee, :CardStatus, :CardType, :ExpiryDate, 
                    :RiskAssessmentScore, :LastPaymentDate, :LastPaymentAmount, :BillingCycle, 
                    :CreditCardIssuer, :CreditCardOfficerID, :CreatedAt, :UpdatedAt)
        """)

        session.execute(insert_statement, creditcard_account_data)
        session.commit()

# Function to populate the `settlement_data` table
def populate_settlement_data(num_records):
    for _ in range(num_records):
        settlement_data = {
            'TransactionID': fake.uuid4(),
            'CustomerID': random.randint(1, num_records),
            'SettlementDate': fake.date_this_decade(),
            'CurrencyCode': random.choice(['USD', 'EUR', 'GBP']),
            'SettlementAmount': round(random.uniform(5000, 100000), 2),
            'FeeAmount': round(random.uniform(10, 100), 2),
            'NetAmount': round(random.uniform(4900, 99500), 2),
            'Status': random.choice(['Completed', 'Pending', 'Failed']),
            'PaymentMethod': random.choice(['Wire Transfer', 'Credit Card', 'ACH']),
            'BeneficiaryName': fake.name(),
            'BeneficiaryAccountNumber': fake.bban(),
            'BeneficiaryBankName': fake.company(),
            'BeneficiaryBankSWIFT': fake.swift(),
            'InitiatingParty': fake.name(),
            'InitiatingPartyAccountNumber': fake.bban(),
            'InitiatingBankName': fake.company(),
            'InitiatingBankSWIFT': fake.swift(),
            'ReferenceNumber': fake.bban(),
            'SettlementType': random.choice(['Standard', 'Priority']),
            'FXRate': round(random.uniform(0.8, 1.5), 4),
            'SettlementInstructions': fake.sentence(),
            'CountryCode': random.choice(['US', 'GB', 'FR']),
            'BankCharges': round(random.uniform(5, 50), 2),
            'AdditionalInfo': fake.text()
        }

        insert_statement = text("""
            INSERT INTO settlement_data (TransactionID, CustomerID, SettlementDate, CurrencyCode, SettlementAmount, FeeAmount, 
                                         NetAmount, Status, PaymentMethod, BeneficiaryName, BeneficiaryAccountNumber, 
                                         BeneficiaryBankName, BeneficiaryBankSWIFT, InitiatingParty, InitiatingPartyAccountNumber, 
                                         InitiatingBankName, InitiatingBankSWIFT, ReferenceNumber, SettlementType, FXRate, 
                                         SettlementInstructions, CountryCode, BankCharges, AdditionalInfo)
            VALUES (:TransactionID, :CustomerID, :SettlementDate, :CurrencyCode, :SettlementAmount, :FeeAmount, 
                    :NetAmount, :Status, :PaymentMethod, :BeneficiaryName, :BeneficiaryAccountNumber, 
                    :BeneficiaryBankName, :BeneficiaryBankSWIFT, :InitiatingParty, :InitiatingPartyAccountNumber, 
                    :InitiatingBankName, :InitiatingBankSWIFT, :ReferenceNumber, :SettlementType, :FXRate, 
                    :SettlementInstructions, :CountryCode, :BankCharges, :AdditionalInfo)
        """)

        session.execute(insert_statement, settlement_data)

# Function to populate the `customer_complaints` table
def populate_customer_complaints(num_records):
    for _ in range(num_records):
        customer_complaint_data = {
            'CustomerID': random.randint(1, num_records),
            'ComplaintDate': fake.date_this_year(),
            'ComplaintCategory': random.choice(['Service Issue', 'Product Issue', 'Billing Issue']),
            'ComplaintDetails': fake.sentence(),
            'ComplaintStatus': random.choice(['Resolved', 'Pending', 'Escalated']),
            'ResolutionDetails': fake.text(),
            'ResolutionDate': date_next_month(),
            'AssignedTo': random.randint(1, num_records),
            'PriorityLevel': random.choice(['High', 'Medium', 'Low']),
            'EscalationLevel': random.choice(['Level 1', 'Level 2', 'Level 3']),
            'ResponseDueDate': fake.date_this_year(),
            'ClosureDate': fake.date_this_year(),
            'CreatedAt': datetime.now(),
            'UpdatedAt': datetime.now()
        }

        insert_statement = text("""
            INSERT INTO Customer_Complaints (CustomerID, ComplaintDate, ComplaintCategory, ComplaintDetails, ComplaintStatus, 
                                             ResolutionDetails, ResolutionDate, AssignedTo, PriorityLevel, EscalationLevel, 
                                             ResponseDueDate, ClosureDate, CreatedAt, UpdatedAt)
            VALUES (:CustomerID, :ComplaintDate, :ComplaintCategory, :ComplaintDetails, :ComplaintStatus, 
                    :ResolutionDetails, :ResolutionDate, :AssignedTo, :PriorityLevel, :EscalationLevel, 
                    :ResponseDueDate, :ClosureDate, :CreatedAt, :UpdatedAt)
        """)

        session.execute(insert_statement, customer_complaint_data)
        session.commit()

def populate_settlement_disputes(num_records):
    for _ in range(num_records):
        dispute_id = str(uuid.uuid4())  # Generate a unique DisputeID
        settlement_dispute_data = {
            'DisputeID': dispute_id,
            'DisputeDate': fake.date_this_decade(),
            'DisputeStatus': random.choice(['Open', 'Closed', 'Escalated']),
            'DisputeReason': fake.sentence(),
            'DisputedAmount': round(random.uniform(100, 5000), 2),
            'ResolutionDate': fake.date_this_decade(),
            'ResolutionDetails': fake.text(),
            'ResponsibleParty': fake.name(),
            'ComplianceCheckStatus': random.choice(['Passed', 'Failed']),
            'RegulatoryApprovalStatus': random.choice(['Approved', 'Pending']),
            'SettlementCorrectionAmount': round(random.uniform(100, 5000), 2),
            'SettlementCorrectionDetails': fake.text(),
            'DisputeNotes': fake.text(),
            'CreatedAt': datetime.now(),
            'UpdatedAt': datetime.now()
        }

        insert_statement = text("""
            INSERT INTO Settlement_Disputes (DisputeID, DisputeDate, DisputeStatus, DisputeReason, DisputedAmount, 
                                             ResolutionDate, ResolutionDetails, ResponsibleParty, ComplianceCheckStatus, 
                                             RegulatoryApprovalStatus, SettlementCorrectionAmount, SettlementCorrectionDetails, 
                                             DisputeNotes, CreatedAt, UpdatedAt)
            VALUES (:DisputeID, :DisputeDate, :DisputeStatus, :DisputeReason, :DisputedAmount, 
                    :ResolutionDate, :ResolutionDetails, :ResponsibleParty, :ComplianceCheckStatus, 
                    :RegulatoryApprovalStatus, :SettlementCorrectionAmount, :SettlementCorrectionDetails, 
                    :DisputeNotes, :CreatedAt, :UpdatedAt)
        """)

        session.execute(insert_statement, settlement_dispute_data)
        session.commit()

# Function to populate the `customer_kyc_details` table
def populate_customer_kyc_details(num_records):
    for _ in range(num_records):
        kyc_details_data = {
            'CustomerID': random.randint(1, num_records),
            'KYCStatus': random.choice(['Verified', 'Pending']),
            'KYCExpiryDate': fake.date_this_decade(),
            'KYCVerificationDate': fake.date_this_year(),
            'IDProofType': random.choice(['Passport', 'Driver\'s License', 'National ID']),
            'IDProofNumber': fake.ssn(),
            'AddressProofType': random.choice(['Utility Bill', 'Bank Statement']),
            'AddressProofNumber': fake.ssn(),
            'RiskCategory': random.choice(['Low', 'Medium', 'High']),
            'PoliticallyExposedPerson': random.choice([True, False]),
            'SourceOfWealth': fake.text(max_nb_chars=255),
            'CreatedAt': datetime.now(),
            'UpdatedAt': datetime.now()
        }

        insert_statement = text("""
            INSERT INTO Customer_KYC_Details (CustomerID, KYCStatus, KYCExpiryDate, KYCVerificationDate, IDProofType, 
                                              IDProofNumber, AddressProofType, AddressProofNumber, RiskCategory, 
                                              PoliticallyExposedPerson, SourceOfWealth, CreatedAt, UpdatedAt)
            VALUES (:CustomerID, :KYCStatus, :KYCExpiryDate, :KYCVerificationDate, :IDProofType, 
                    :IDProofNumber, :AddressProofType, :AddressProofNumber, :RiskCategory, 
                    :PoliticallyExposedPerson, :SourceOfWealth, :CreatedAt, :UpdatedAt)
        """)

        session.execute(insert_statement, kyc_details_data)
        session.commit()

# Function to populate the `transaction_charges` table
def populate_transaction_charges(num_records):
    for _ in range(num_records):
        transaction_charge_data = {
            'TransactionID': random.randint(1, num_records),
            'ChargeType': random.choice(['Processing Fee', 'Service Charge', 'Foreign Exchange Fee']),
            'ChargeAmount': round(random.uniform(10, 100), 2),
            'ChargeCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'ChargeDate': fake.date_this_year(),
            'ChargeStatus': random.choice(['Applied', 'Waived', 'Refunded']),
            'TaxAmount': round(random.uniform(1, 10), 2),
            'TaxRate': round(random.uniform(0, 20), 2),
            'TotalChargeAmount': round(random.uniform(10, 200), 2),
            'ChargeDescription': fake.sentence(),
            'WaiverReason': fake.sentence(),
            'AppliedBy': fake.name(),
            'SettlementID': random.randint(1, num_records),
            'RegulatoryCompliance': random.choice(['Compliant', 'Non-Compliant']),
            'ChargeApprovalStatus': random.choice(['Approved', 'Pending']),
            'Notes': fake.text(),
            'CreatedAt': datetime.now(),
            'UpdatedAt': datetime.now()
        }

        insert_statement = text("""
            INSERT INTO Transaction_Charges (TransactionID, ChargeType, ChargeAmount, ChargeCurrency, ChargeDate, ChargeStatus, 
                                             TaxAmount, TaxRate, TotalChargeAmount, ChargeDescription, WaiverReason, AppliedBy, 
                                             SettlementID, RegulatoryCompliance, ChargeApprovalStatus, Notes, CreatedAt, UpdatedAt)
            VALUES (:TransactionID, :ChargeType, :ChargeAmount, :ChargeCurrency, :ChargeDate, :ChargeStatus, 
                    :TaxAmount, :TaxRate, :TotalChargeAmount, :ChargeDescription, :WaiverReason, :AppliedBy, 
                    :SettlementID, :RegulatoryCompliance, :ChargeApprovalStatus, :Notes, :CreatedAt, :UpdatedAt)
        """)

        session.execute(insert_statement, transaction_charge_data)
        session.commit()

# Function to populate the `customer_master` table
def populate_customer_master(num_records):
    for _ in range(num_records):
        customer_data = {
            'CustomerName': fake.name(),
            'AccountNumber': fake.bban(),
            'AccountType': random.choice(['Savings', 'Current', 'Fixed Deposit']),
            'Address': fake.address(),
            'ContactNumber': fake.phone_number(),
            'Email': fake.email(),
            'DateOfBirth': fake.date_of_birth(minimum_age=18, maximum_age=75),
            'CustomerSince': fake.date_this_decade(),
            'Status': random.choice(['Active', 'Dormant', 'Closed']),
            'NationalID': fake.ssn(),
            'TaxID': fake.ssn(),
            'EmploymentStatus': random.choice(['Employed', 'Self-Employed', 'Unemployed', 'Retired']),
            'AnnualIncome': round(random.uniform(30000, 150000), 2),
            'RiskProfile': random.choice(['Low', 'Medium', 'High']),
            'MaritalStatus': random.choice(['Single', 'Married', 'Divorced']),
            'NumberOfDependents': random.randint(0, 4),
            'PreferredLanguage': random.choice(['English', 'Spanish', 'French']),
            'PreferredCommunicationChannel': random.choice(['Email', 'Phone', 'SMS']),
        }

        insert_statement = text("""
            INSERT INTO customer_master (CustomerName, AccountNumber, AccountType, Address, ContactNumber, Email, DateOfBirth,
                                         CustomerSince, Status, NationalID, TaxID, EmploymentStatus, AnnualIncome, RiskProfile,
                                         MaritalStatus, NumberOfDependents, PreferredLanguage, PreferredCommunicationChannel)
            VALUES (:CustomerName, :AccountNumber, :AccountType, :Address, :ContactNumber, :Email, :DateOfBirth, :CustomerSince,
                    :Status, :NationalID, :TaxID, :EmploymentStatus, :AnnualIncome, :RiskProfile, :MaritalStatus, :NumberOfDependents,
                    :PreferredLanguage, :PreferredCommunicationChannel)
        """)

        session.execute(insert_statement, customer_data)

def date_next_year():
    today = datetime.today()
    next_year = today + timedelta(days=365)
    return next_year.date()
# Function to populate the `transaction_fees` table
def populate_transaction_fees(num_records):
    for _ in range(num_records):
        transaction_fee_data = {
            'TransactionID': random.randint(1, num_records),
            'FeeType': random.choice(['Processing Fee', 'Service Fee', 'Foreign Exchange Fee']),
            'FeeAmount': round(random.uniform(10, 500), 2),
            'FeeCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'FeeDate': fake.date_this_year(),
            'FeeStatus': random.choice(['Charged', 'Waived', 'Refunded']),
            'TaxAmount': round(random.uniform(1, 50), 2),
            'TaxRate': round(random.uniform(0.1, 5.0), 2),
            'TotalFeeAmount': round(random.uniform(10, 550), 2),
            'FeeDescription': fake.text(max_nb_chars=255),
            'WaiverReason': fake.text(max_nb_chars=255),
            'RegulatoryCompliance': random.choice(['Compliant', 'Non-Compliant']),
            'AppliedBy': fake.name(),
            'SettlementID': random.randint(1, num_records),
            'Notes': fake.text(),
        }

        insert_statement = text("""
            INSERT INTO Transaction_Fees (TransactionID, FeeType, FeeAmount, FeeCurrency, FeeDate, FeeStatus, 
                                         TaxAmount, TaxRate, TotalFeeAmount, FeeDescription, WaiverReason, 
                                         RegulatoryCompliance, AppliedBy, SettlementID, Notes)
            VALUES (:TransactionID, :FeeType, :FeeAmount, :FeeCurrency, :FeeDate, :FeeStatus, 
                    :TaxAmount, :TaxRate, :TotalFeeAmount, :FeeDescription, :WaiverReason, 
                    :RegulatoryCompliance, :AppliedBy, :SettlementID, :Notes)
        """)

        session.execute(insert_statement, transaction_fee_data)
        session.commit()

# Function to populate the `customer_risk` table
def populate_customer_risk(num_records):
    for _ in range(num_records):
        customer_risk_data = {
            'CustomerID': random.randint(1, num_records),
            'RiskCategory': random.choice(['Low', 'Medium', 'High']),
            'RiskScore': random.randint(1, 100),
            'RiskAssessmentDate': fake.date_this_year(),
            'ReviewDate': date_next_year()
        }

        insert_statement = text("""
            INSERT INTO Customer_Risk_Profile (CustomerID, RiskCategory, RiskScore, RiskAssessmentDate, ReviewDate)
            VALUES (:CustomerID, :RiskCategory, :RiskScore, :RiskAssessmentDate, :ReviewDate)
        """)

        session.execute(insert_statement, customer_risk_data)
        session.commit()

# Function to populate the `transaction_master` table
def populate_transaction_master(num_records):
    for _ in range(num_records):
        transaction_master_data = {
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'TransactionAmount': round(random.uniform(100, 10000), 2),
            'TransactionDate': fake.date_this_year(),
            'TransactionType': random.choice(['Deposit', 'Withdrawal', 'Transfer']),
            'TransactionStatus': random.choice(['Completed', 'Pending', 'Failed']),
            'CurrencyCode': random.choice(['USD', 'EUR', 'GBP']),
            'ReferenceNumber': fake.bban(),
            'MerchantName': fake.company(),
            'MerchantCategoryCode': fake.random_number(digits=4, fix_len=True),
            'TransactionDescription': fake.sentence(),
            'PaymentMethod': random.choice(['Credit Card', 'Bank Transfer']),
            'TransactionSource': random.choice(['Online', 'In-branch']),
            'TransactionMode': random.choice(['One-time', 'Recurring']),
            'AuthorizationCode': fake.bban(),
            'RiskAssessmentScore': random.randint(1, 100),
            'ProcessingTime': datetime.now(),
            'TransactionChannel': random.choice(['Mobile', 'Web']),
            'SettlementID': random.randint(1, num_records),
            'FeeAmount': round(random.uniform(1, 100), 2),
            'TaxAmount': round(random.uniform(1, 100), 2),
            'BalanceAfterTransaction': round(random.uniform(1000, 100000), 2)
        }

        insert_statement = text("""
            INSERT INTO Transaction_Master (CustomerID, AccountID, TransactionAmount, TransactionDate, TransactionType, 
                                            TransactionStatus, CurrencyCode, ReferenceNumber, MerchantName, 
                                            MerchantCategoryCode, TransactionDescription, PaymentMethod, 
                                            TransactionSource, TransactionMode, AuthorizationCode, RiskAssessmentScore, 
                                            ProcessingTime, TransactionChannel, SettlementID, FeeAmount, TaxAmount, 
                                            BalanceAfterTransaction)
            VALUES (:CustomerID, :AccountID, :TransactionAmount, :TransactionDate, :TransactionType, 
                    :TransactionStatus, :CurrencyCode, :ReferenceNumber, :MerchantName, 
                    :MerchantCategoryCode, :TransactionDescription, :PaymentMethod, 
                    :TransactionSource, :TransactionMode, :AuthorizationCode, :RiskAssessmentScore, 
                    :ProcessingTime, :TransactionChannel, :SettlementID, :FeeAmount, :TaxAmount, 
                    :BalanceAfterTransaction)
        """)

        session.execute(insert_statement, transaction_master_data)
        session.commit()

# Function to populate the `customer_transaction_history` table
def populate_customer_transaction_history(num_records):
    for _ in range(num_records):
        transaction_history_data = {
            'TransactionID': str(uuid.uuid4()),  # Generate a unique UUID for TransactionID
            'CustomerID': random.randint(1, num_records),
            'AccountID': random.randint(1, num_records),
            'TransactionDate': fake.date_this_year(),
            'TransactionType': random.choice(['Debit', 'Credit']),
            'TransactionAmount': round(random.uniform(100, 10000), 2),
            'TransactionCurrency': random.choice(['USD', 'EUR', 'GBP']),
            'TransactionStatus': random.choice(['Completed', 'Pending', 'Failed']),
            'MerchantName': fake.company(),
            'MerchantCategory': fake.word(),
            'ReferenceNumber': fake.bban(),
            'TransactionMode': random.choice(['One-time', 'Recurring']),
            'TransactionDescription': fake.sentence(),
            'FeeAmount': round(random.uniform(1, 100), 2),
            'TaxAmount': round(random.uniform(1, 100), 2),
            'BalanceAfterTransaction': round(random.uniform(1000, 100000), 2)
        }

        insert_statement = text("""
            INSERT INTO Customer_Transaction_History (TransactionID, CustomerID, AccountID, TransactionDate, 
                                                      TransactionType, TransactionAmount, TransactionCurrency, 
                                                      TransactionStatus, MerchantName, MerchantCategory, 
                                                      ReferenceNumber, TransactionMode, TransactionDescription, 
                                                      FeeAmount, TaxAmount, BalanceAfterTransaction)
            VALUES (:TransactionID, :CustomerID, :AccountID, :TransactionDate, :TransactionType, 
                    :TransactionAmount, :TransactionCurrency, :TransactionStatus, :MerchantName, 
                    :MerchantCategory, :ReferenceNumber, :TransactionMode, :TransactionDescription, 
                    :FeeAmount, :TaxAmount, :BalanceAfterTransaction)
        """)

        session.execute(insert_statement, transaction_history_data)
        session.commit()

def populate_loan_accounts(num_records):
    used_ids = set()
    used_account_numbers = set()
    
    for _ in range(num_records):
        while True:
            loan_account_id = random.randint(1, num_records * 10)
            if loan_account_id not in used_ids:
                used_ids.add(loan_account_id)
                break
        
        while True:
            account_number = fake.bban()
            if account_number not in used_account_numbers:
                used_account_numbers.add(account_number)
                break
        
        loan_account_data = {
            'LoanAccountID': loan_account_id,
            'ApplicationID': random.randint(1, num_records),
            'CustomerID': random.randint(1, num_records),
            'AccountNumber': account_number,
            'LoanAmount': round(random.uniform(1000, 100000), 2),
            'DisbursementDate': fake.date_this_decade(),
            'LoanTermInMonths': random.randint(12, 360),
            'InterestRate': round(random.uniform(1.0, 15.0), 2),
            'OutstandingPrincipal': round(random.uniform(1000, 100000), 2),
            'NextRepaymentDate': fake.date_this_decade(),
            'RepaymentFrequency': random.choice(['Monthly', 'Quarterly']),
            'LoanStatus': random.choice(['Active', 'Closed', 'Defaulted']),
            'CollateralDetails': fake.text(),
            'PenaltyRate': round(random.uniform(0.5, 5.0), 2),
            'GracePeriodInDays': random.randint(0, 90),
            'EarlyRepaymentPenalty': round(random.uniform(0, 1000), 2),
            'LoanPurpose': fake.sentence(),
            'RiskGrade': random.choice(['A', 'B', 'C', 'D', 'E']),
            'LoanOfficerID': random.randint(1, num_records),
            'LastPaymentDate': fake.date_this_decade(),
            'LastPaymentAmount': round(random.uniform(100, 10000), 2),
        }

        insert_statement = text("""
            INSERT INTO Loan_Accounts (LoanAccountID, ApplicationID, CustomerID, AccountNumber, LoanAmount, 
                                       DisbursementDate, LoanTermInMonths, InterestRate, OutstandingPrincipal, 
                                       NextRepaymentDate, RepaymentFrequency, LoanStatus, CollateralDetails, 
                                       PenaltyRate, GracePeriodInDays, EarlyRepaymentPenalty, LoanPurpose, 
                                       RiskGrade, LoanOfficerID, LastPaymentDate, LastPaymentAmount)
            VALUES (:LoanAccountID, :ApplicationID, :CustomerID, :AccountNumber, :LoanAmount, 
                    :DisbursementDate, :LoanTermInMonths, :InterestRate, :OutstandingPrincipal, 
                    :NextRepaymentDate, :RepaymentFrequency, :LoanStatus, :CollateralDetails, 
                    :PenaltyRate, :GracePeriodInDays, :EarlyRepaymentPenalty, :LoanPurpose, 
                    :RiskGrade, :LoanOfficerID, :LastPaymentDate, :LastPaymentAmount)
        """)

        session.execute(insert_statement, loan_account_data)
    
    session.commit()
    print("All loan account records inserted successfully.")

# Function to execute all population functions
def populate_all_tables(num_records):
    populate_customer_master(num_records)
    populate_settlement_data(num_records)
    populate_clearing_houses(num_records)
    populate_direct_debits(num_records)
    populate_recurring_payments(num_records)
    populate_employee_details(num_records)
    populate_settlement_partners(num_records)
    populate_fixed_deposit_accounts(num_records)
    populate_settlement_reconciliation(num_records)
    populate_forex_transactions(num_records)
    populate_standing_orders(num_records)
    populate_fraud_alerts(num_records)
    populate_account_balances(num_records)
    populate_international_payments(num_records)
    populate_account_holder(num_records)
    populate_investment_accounts(num_records)
    populate_account_master(num_records)
    populate_loan_accounts(num_records)
    populate_account_statement(num_records)
    populate_loan_applications(num_records)
    populate_anti_money_laundering_reports(num_records)
    populate_loan_collateral_details(num_records)
    populate_audit_logs(num_records)
    populate_loan_defaults(num_records)
    populate_bank_charges(num_records)
    populate_loan_interest_details(num_records)
    populate_branch_details(num_records)
    populate_loan_repayment_schedules(num_records)
    populate_cheque_clearing(num_records)
    populate_mortgage_accounts(num_records)
    populate_commercial_lending(num_records)
    populate_overdraft_accounts(num_records)
    populate_compliance_logs(num_records)
    populate_payment_instructions(num_records)
    populate_contact_details(num_records)
    populate_regulatory_reports(num_records)
    populate_corporate_accounts(num_records)
    populate_risk_exposure(num_records)
    populate_credit_score_reports(num_records)
    populate_savings_account(num_records)
    populate_creditcard_accounts(num_records)
    populate_settlement_data(num_records)
    populate_customer_complaints(num_records)
    populate_settlement_disputes(num_records)
    populate_customer_kyc_details(num_records)
    populate_transaction_charges(num_records)
    populate_customer_master(num_records)
    populate_transaction_fees(num_records)
    populate_customer_risk(num_records)
    populate_transaction_master(num_records)
    populate_customer_transaction_history(num_records)
    # Add calls to other populate functions here

# Execute SQL files to create tables
execute_sql_files()

# Populate all tables with dummy data (specify the number of records here)
populate_all_tables(1000)

# Commit and close the session
session.commit()
session.close()

print("All tables created and populated with dummy data!")
