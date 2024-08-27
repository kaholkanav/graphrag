CREATE TABLE IF NOT EXISTS Corporate_Accounts (
    CorporateAccountID INT PRIMARY KEY,
    CompanyName VARCHAR(255),
    AccountNumber VARCHAR(20) UNIQUE,
    BranchCode VARCHAR(10),
    AccountType VARCHAR(50), -- e.g., Current, Savings
    AccountStatus VARCHAR(50), -- e.g., Active, Dormant, Closed
    AccountBalance DECIMAL(15, 2),
    AuthorizedSignatories TEXT,
    TaxID VARCHAR(50),
    AccountOpeningDate DATE,
    AccountClosureDate DATE,
    AccountManagerID INT,
    RiskAssessmentScore INT,
    TransactionLimitPerDay DECIMAL(15, 2),
    OverdraftFacility BOOLEAN,
    OverdraftLimit DECIMAL(15, 2),
    LoanEligibility BOOLEAN,
    LoanLimit DECIMAL(15, 2),
    AccountTier VARCHAR(50),
    ComplianceOfficer VARCHAR(100),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
