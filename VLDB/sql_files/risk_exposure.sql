CREATE TABLE Risk_Exposure (
    RiskExposureID INT PRIMARY KEY,
    CustomerID INT,
    AccountID INT,
    ExposureDate DATE,
    RiskType VARCHAR(50), -- e.g., Credit Risk, Liquidity Risk, Market Risk
    RiskScore INT,
    RiskMitigationStrategy VARCHAR(255),
    ExposureAmount DECIMAL(15, 2),
    ExposureCurrency VARCHAR(3),
    ExposureStatus VARCHAR(50), -- e.g., Active, Resolved, Escalated
    ResolutionDate DATE,
    ResolutionDetails TEXT,
    RiskOfficer VARCHAR(100),
    ComplianceCheckStatus VARCHAR(50),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID)
);
