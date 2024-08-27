CREATE TABLE Standing_Orders (
    StandingOrderID INT PRIMARY KEY,
    CustomerID INT,
    AccountID INT,
    OrderStartDate DATE,
    OrderEndDate DATE,
    RecurrencePattern VARCHAR(50), -- e.g., Monthly, Weekly
    OrderAmount DECIMAL(15, 2),
    OrderCurrency VARCHAR(3),
    BeneficiaryName VARCHAR(100),
    BeneficiaryAccountNumber VARCHAR(20),
    BeneficiaryBankName VARCHAR(100),
    BeneficiaryBankSWIFT VARCHAR(20),
    ReferenceNumber VARCHAR(50),
    OrderStatus VARCHAR(50), -- e.g., Active, Suspended, Cancelled
    PaymentMethod VARCHAR(50), -- e.g., Bank Transfer, Direct Debit
    NextOrderDate DATE,
    TransactionID INT,
    RiskAssessmentScore INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
