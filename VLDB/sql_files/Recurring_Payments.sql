CREATE TABLE Recurring_Payments (
    RecurringPaymentID INT PRIMARY KEY,
    CustomerID INT,
    AccountID INT,
    RecurrencePattern VARCHAR(50), -- e.g., Monthly, Weekly
    PaymentAmount DECIMAL(15, 2),
    PaymentCurrency VARCHAR(3),
    FirstPaymentDate DATE,
    NextPaymentDate DATE,
    EndDate DATE,
    BeneficiaryName VARCHAR(100),
    BeneficiaryAccountNumber VARCHAR(20),
    BeneficiaryBankName VARCHAR(100),
    BeneficiaryBankSWIFT VARCHAR(20),
    PaymentStatus VARCHAR(50), -- e.g., Active, Inactive
    PaymentMethod VARCHAR(50), -- e.g., Bank Transfer, Direct Debit
    PaymentReference VARCHAR(50),
    RiskAssessmentScore INT,
    Notes TEXT,
    TransactionID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
