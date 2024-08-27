CREATE TABLE Commercial_Lending (
    LendingID INT PRIMARY KEY,
    CorporateAccountID INT,
    LoanType VARCHAR(50), -- e.g., Working Capital, Term Loan
    LoanAmount DECIMAL(15, 2),
    DisbursementDate DATE,
    RepaymentTermInMonths INT,
    InterestRate DECIMAL(5, 2),
    RepaymentSchedule VARCHAR(50), -- e.g., Monthly, Quarterly
    LoanStatus VARCHAR(50), -- e.g., Active, Closed, Defaulted
    CollateralDetails TEXT,
    RiskAssessmentScore INT,
    GracePeriodInMonths INT,
    PenaltyForLatePayment DECIMAL(10, 2),
    EarlyRepaymentPenalty DECIMAL(10, 2),
    LoanOfficer VARCHAR(100),
    LoanPurpose VARCHAR(255),
    RegulatoryComplianceStatus VARCHAR(50),
    CreditRating VARCHAR(50),
    AccountManagerID INT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CorporateAccountID) REFERENCES Corporate_Accounts(CorporateAccountID)
);
