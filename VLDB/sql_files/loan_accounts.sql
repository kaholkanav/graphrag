CREATE TABLE Loan_Accounts (
    LoanAccountID INT PRIMARY KEY,
    ApplicationID INT,
    CustomerID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    LoanAmount DECIMAL(15, 2),
    DisbursementDate DATE,
    LoanTermInMonths INT,
    InterestRate DECIMAL(5, 2),
    OutstandingPrincipal DECIMAL(15, 2),
    NextRepaymentDate DATE,
    RepaymentFrequency VARCHAR(20), -- e.g., Monthly, Quarterly
    LoanStatus VARCHAR(50), -- e.g., Active, Closed, Defaulted
    CollateralDetails TEXT,
    PenaltyRate DECIMAL(5, 2),
    GracePeriodInDays INT,
    EarlyRepaymentPenalty DECIMAL(10, 2),
    LoanPurpose VARCHAR(255),
    RiskGrade VARCHAR(50),
    LoanOfficerID INT,
    LastPaymentDate DATE,
    LastPaymentAmount DECIMAL(15, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ApplicationID) REFERENCES Loan_Applications(ApplicationID),
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
