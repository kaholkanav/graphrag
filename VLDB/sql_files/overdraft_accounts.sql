CREATE TABLE Overdraft_Accounts (
    OverdraftAccountID INT PRIMARY KEY,
    CustomerID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    ApprovedLimit DECIMAL(15, 2),
    CurrentOverdraftBalance DECIMAL(15, 2),
    InterestRate DECIMAL(5, 2),
    OverdraftStartDate DATE,
    OverdraftEndDate DATE,
    OverdraftStatus VARCHAR(50), -- e.g., Active, Inactive
    FeeAmount DECIMAL(10, 2),
    PenaltyRate DECIMAL(5, 2),
    NextReviewDate DATE,
    RiskAssessmentScore INT,
    CollateralDetails TEXT,
    CreditScore INT,
    OverdraftOfficerID INT,
    IsSecured BOOLEAN,
    CollateralID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (CollateralID) REFERENCES Loan_Collateral_Details(CollateralID)
);
