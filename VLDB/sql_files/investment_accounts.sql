CREATE TABLE Investment_Accounts (
    InvestmentAccountID INT PRIMARY KEY,
    CustomerID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    InvestmentType VARCHAR(50), -- e.g., Mutual Fund, Stock Portfolio
    InvestmentAmount DECIMAL(15, 2),
    RiskProfile VARCHAR(50),
    PortfolioManager VARCHAR(100),
    AccountStatus VARCHAR(50), -- e.g., Active, Closed
    LastValuationDate DATE,
    CurrentValue DECIMAL(15, 2),
    ReturnOnInvestment DECIMAL(5, 2),
    InvestmentStartDate DATE,
    InvestmentEndDate DATE,
    InvestmentTermInMonths INT,
    RegulatoryComplianceStatus VARCHAR(50),
    TaxWithheld DECIMAL(15, 2),
    AccountManagerID INT,
    TransactionLimitPerDay DECIMAL(15, 2),
    DividendPayoutFrequency VARCHAR(50), -- e.g., Quarterly, Annually
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
