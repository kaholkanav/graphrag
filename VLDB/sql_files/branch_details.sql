CREATE TABLE Branch_Details (
    BranchID INT PRIMARY KEY,
    BranchCode VARCHAR(10) UNIQUE,
    BranchName VARCHAR(100),
    BranchAddress VARCHAR(255),
    BranchPhoneNumber VARCHAR(20),
    BranchManager VARCHAR(100),
    Region VARCHAR(50),
    OperatingHours VARCHAR(100),
    NumberOfEmployees INT,
    RegulatoryComplianceStatus VARCHAR(50),
    LastAuditDate DATE,
    RiskAssessmentScore INT,
    CustomerServiceRating DECIMAL(5, 2),
    NumberOfAccounts INT,
    BranchEmail VARCHAR(100),
    BranchStatus VARCHAR(50), -- e.g., Open, Closed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
