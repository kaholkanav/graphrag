CREATE TABLE Account_Balances (
    BalanceID INT PRIMARY KEY,
    AccountID INT,
    BalanceDate DATE,
    OpeningBalance DECIMAL(15, 2),
    ClosingBalance DECIMAL(15, 2),
    AvailableBalance DECIMAL(15, 2),
    BlockedAmount DECIMAL(15, 2),
    OverdraftLimit DECIMAL(15, 2),
    InterestEarned DECIMAL(10, 2),
    ChargesIncurred DECIMAL(10, 2),
    BalanceType VARCHAR(20), -- e.g., Daily, Monthly
    CurrencyCode VARCHAR(3),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID)
);
