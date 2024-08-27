CREATE TABLE Mortgage_Accounts (
    MortgageAccountID INT PRIMARY KEY,
    CustomerID INT,
    ApplicationID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    PropertyValue DECIMAL(15, 2),
    LoanAmount DECIMAL(15, 2),
    InterestRate DECIMAL(5, 2),
    LoanTermInYears INT,
    RepaymentSchedule VARCHAR(50), -- e.g., Monthly, Quarterly
    MortgageStatus VARCHAR(50), -- e.g., Active, Closed, Defaulted
    CollateralDetails TEXT,
    PropertyAddress VARCHAR(255),
    PropertyType VARCHAR(50), -- e.g., Residential, Commercial
    LienStatus VARCHAR(50), -- e.g., First Lien, Second Lien
    RiskGrade VARCHAR(50),
    AppraisalValue DECIMAL(15, 2),
    AppraisalDate DATE,
    InsuranceAmount DECIMAL(15, 2),
    InsuranceExpiryDate DATE,
    MortgageOfficerID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ApplicationID) REFERENCES Loan_Applications(ApplicationID)
);
