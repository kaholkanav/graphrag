CREATE TABLE Fraud_Alerts (
    FraudAlertID INT PRIMARY KEY,
    TransactionID INT,
    CustomerID INT,
    AlertDate DATE,
    AlertType VARCHAR(50), -- e.g., High Risk, Medium Risk
    RiskScore INT,
    AlertStatus VARCHAR(50), -- e.g., Investigating, Resolved, Escalated
    TriggeredBy VARCHAR(100), -- e.g., Rule-Based, ML Model
    InvestigationStartDate DATE,
    InvestigationEndDate DATE,
    FraudType VARCHAR(50), -- e.g., Identity Theft, Account Takeover
    ResolutionStatus VARCHAR(50), -- e.g., Resolved, Unresolved
    ResolutionDetails TEXT,
    InvestigativeFindings TEXT,
    ReportToAuthorities BOOLEAN,
    Notes TEXT,
    ComplianceCheckStatus VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID),
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
