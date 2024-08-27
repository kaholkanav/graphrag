CREATE TABLE Fixed_Deposit_Accounts (
    FixedDepositID INT PRIMARY KEY,
    CustomerID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    DepositAmount DECIMAL(15, 2),
    InterestRate DECIMAL(5, 2),
    DepositTermInMonths INT,
    MaturityDate DATE,
    MaturityAmount DECIMAL(15, 2),
    InterestPaymentFrequency VARCHAR(50), -- e.g., Monthly, Quarterly
    PenaltyForEarlyWithdrawal DECIMAL(10, 2),
    WithdrawalRestrictions VARCHAR(255),
    AutoRenewal BOOLEAN,
    NomineeName VARCHAR(100),
    NomineeRelation VARCHAR(50),
    DepositStartDate DATE,
    DepositEndDate DATE,
    DepositStatus VARCHAR(50), -- e.g., Active, Matured, Closed
    AccountManagerID INT,
    TaxWithheld DECIMAL(15, 2),
    RegulatoryComplianceStatus VARCHAR(50),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
