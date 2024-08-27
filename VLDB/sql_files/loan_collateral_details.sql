CREATE TABLE Loan_Collateral_Details (
    CollateralID INT PRIMARY KEY,
    LoanAccountID INT,
    CollateralType VARCHAR(50), -- e.g., Real Estate, Vehicle, Savings
    CollateralValue DECIMAL(15, 2),
    ValuationDate DATE,
    ValuationMethod VARCHAR(50),
    OwnershipProof VARCHAR(255),
    CollateralStatus VARCHAR(50), -- e.g., Held, Released
    InsuredAmount DECIMAL(15, 2),
    InsuranceExpiryDate DATE,
    RiskAssessmentScore INT,
    LienHolderName VARCHAR(100),
    LienHolderContact VARCHAR(100),
    CollateralLocation VARCHAR(255),
    CollateralCondition VARCHAR(50),
    AppraiserName VARCHAR(100),
    AppraisalDate DATE,
    AppraisalReport VARCHAR(255),
    CollateralRegistrationNumber VARCHAR(50),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (LoanAccountID) REFERENCES Loan_Accounts(LoanAccountID)
);
