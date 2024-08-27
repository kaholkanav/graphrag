CREATE TABLE Compliance_Logs (
    ComplianceLogID INT PRIMARY KEY,
    LogDate DATE,
    LogType VARCHAR(50), -- e.g., AML Check, KYC Check, Regulatory Audit
    CustomerID INT,
    AccountID INT,
    TransactionID INT,
    ComplianceStatus VARCHAR(50), -- e.g., Passed, Failed, Under Review
    ComplianceDetails TEXT,
    RegulatoryApprovalStatus VARCHAR(50),
    ReportingOfficer VARCHAR(100),
    EscalationStatus VARCHAR(50),
    InvestigationDetails TEXT,
    ResolutionStatus VARCHAR(50),
    ResolutionDate DATE,
    ResolutionDetails TEXT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
