CREATE TABLE Loan_Interest_Rates (
    InterestRateID INT PRIMARY KEY,
    LoanAccountID INT,
    InterestType VARCHAR(50), -- e.g., Fixed, Variable
    InterestRate DECIMAL(5, 2),
    EffectiveDate DATE,
    ExpiryDate DATE,
    RateChangeFrequency VARCHAR(50),
    RateMargin DECIMAL(5, 2),
    BaseRate DECIMAL(5, 2),
    PenaltyRate DECIMAL(5, 2),
    RiskAdjustedRate DECIMAL(5, 2),
    IsRateCapped BOOLEAN,
    RateCap DECIMAL(5, 2),
    RateFloor DECIMAL(5, 2),
    AnnualPercentageRate DECIMAL(5, 2),
    InterestCompoundingFrequency VARCHAR(50), -- e.g., Monthly, Quarterly
    RateHistory TEXT,
    RateChangeApprovalStatus VARCHAR(50),
    ApprovedBy VARCHAR(100),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (LoanAccountID) REFERENCES Loan_Accounts(LoanAccountID)
);
