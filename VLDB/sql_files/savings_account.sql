CREATE TABLE Savings_Accounts (
    SavingsAccountID INT PRIMARY KEY,
    CustomerID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    BranchCode VARCHAR(10),
    AccountStatus VARCHAR(50), -- e.g., Active, Dormant, Closed
    AccountBalance DECIMAL(15, 2),
    InterestRate DECIMAL(5, 2),
    MinimumBalance DECIMAL(15, 2),
    PenaltyForBelowMinBalance DECIMAL(10, 2),
    LastTransactionDate DATE,
    OverdraftFacility BOOLEAN,
    OverdraftLimit DECIMAL(15, 2),
    AccountTier VARCHAR(50),
    AccountType VARCHAR(50), -- e.g., Regular, Premium
    NomineeName VARCHAR(100),
    NomineeRelation VARCHAR(50),
    AccountOpeningDate DATE,
    AccountClosureDate DATE,
    AccountManagerID INT,
    TransactionLimitPerDay DECIMAL(15, 2),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
