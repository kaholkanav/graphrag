CREATE TABLE Direct_Debits (
    DirectDebitID INT PRIMARY KEY,
    CustomerID INT,
    AccountID INT,
    DebitAmount DECIMAL(15, 2),
    DebitDate DATE,
    RecurrencePattern VARCHAR(50), -- e.g., Monthly, Quarterly
    BeneficiaryName VARCHAR(100),
    BeneficiaryAccountNumber VARCHAR(20),
    BeneficiaryBankName VARCHAR(100),
    BeneficiaryBankSWIFT VARCHAR(20),
    ReferenceNumber VARCHAR(50),
    AuthorizationCode VARCHAR(50),
    DebitStatus VARCHAR(50), -- e.g., Active, Cancelled
    TransactionID INT,
    PaymentMethod VARCHAR(50), -- e.g., Bank Transfer, Credit Card
    RiskAssessmentScore INT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
