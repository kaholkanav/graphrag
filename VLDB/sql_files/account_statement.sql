CREATE TABLE Account_Statements (
    StatementID INT PRIMARY KEY,
    AccountID INT,
    StatementDate DATE,
    StatementPeriodStart DATE,
    StatementPeriodEnd DATE,
    OpeningBalance DECIMAL(15, 2),
    ClosingBalance DECIMAL(15, 2),
    TotalCredits DECIMAL(15, 2),
    TotalDebits DECIMAL(15, 2),
    InterestEarned DECIMAL(10, 2),
    ChargesIncurred DECIMAL(10, 2),
    StatementStatus VARCHAR(20),
    StatementFilePath VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID)
);
