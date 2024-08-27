CREATE TABLE Loan_Repayment_Schedules (
    RepaymentID INT PRIMARY KEY,
    LoanAccountID INT,
    PaymentDueDate DATE,
    PrincipalAmountDue DECIMAL(15, 2),
    InterestAmountDue DECIMAL(15, 2),
    PenaltyAmountDue DECIMAL(10, 2),
    TotalAmountDue DECIMAL(15, 2),
    PaymentStatus VARCHAR(50), -- e.g., Pending, Paid, Overdue
    PaymentDate DATE,
    PaymentAmount DECIMAL(15, 2),
    LateFee DECIMAL(10, 2),
    PaymentMethod VARCHAR(50),
    ReferenceNumber VARCHAR(50),
    RemainingBalance DECIMAL(15, 2),
    InstallmentNumber INT,
    IsGracePeriod BOOLEAN,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (LoanAccountID) REFERENCES Loan_Accounts(LoanAccountID)
);
