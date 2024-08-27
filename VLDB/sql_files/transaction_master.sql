CREATE TABLE Transaction_Master (
    TransactionID INT PRIMARY KEY,
    AccountID INT,
    CustomerID INT,
    TransactionDate DATE,
    TransactionType VARCHAR(50), -- e.g., Deposit, Withdrawal, Transfer
    TransactionAmount DECIMAL(15, 2),
    CurrencyCode VARCHAR(3),
    TransactionStatus VARCHAR(50), -- e.g., Completed, Pending, Failed
    ReferenceNumber VARCHAR(50),
    MerchantName VARCHAR(100),
    MerchantCategoryCode VARCHAR(10),
    TransactionDescription VARCHAR(255),
    PaymentMethod VARCHAR(50), -- e.g., Credit Card, Bank Transfer
    TransactionSource VARCHAR(50), -- e.g., Online, In-branch
    TransactionMode VARCHAR(50), -- e.g., One-time, Recurring
    AuthorizationCode VARCHAR(50),
    RiskAssessmentScore INT,
    ProcessingTime TIMESTAMP,
    TransactionChannel VARCHAR(50), -- e.g., Mobile, Web
    SettlementID INT,
    FeeAmount DECIMAL(10, 2),
    TaxAmount DECIMAL(10, 2),
    BalanceAfterTransaction DECIMAL(15, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
